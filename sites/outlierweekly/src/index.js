// Outlier Weekly owned hub router (worker-first).
// Do not blanket-301 the apex. That was the 2026-08-08 SEO defect.
// Letters stay on Substack; the apex serves owned HTML via Workers assets.

import {
  MFG_CONFIG,
  MFG_SECTIONS,
  MFG_ALLERGENS,
  MFG_STEPS,
  MFG_DISHES,
} from "./mfg-data.js";

const SUBSTACK_BASE = "https://outlierweekly.substack.com";
const APEX_HOST = "outlierweekly.com";
const WWW_HOST = "www.outlierweekly.com";

const SECURITY_HEADERS = {
  "Strict-Transport-Security": "max-age=63072000; includeSubDomains",
  "X-Content-Type-Options": "nosniff",
  "Referrer-Policy": "strict-origin-when-cross-origin",
};

function stripTrailingSlash(pathname) {
  if (pathname.length > 1 && pathname.endsWith("/")) {
    return pathname.slice(0, -1);
  }
  return pathname;
}

// Paths that belong to the Substack publication, not the owned hub.
function isSubstackPath(pathname) {
  const p = stripTrailingSlash(pathname);
  return (
    p.startsWith("/p/") ||
    p === "/p" ||
    p === "/subscribe" ||
    p === "/feed" ||
    p === "/archive"
  );
}

// Unlisted surfaces: not in sitemap.xml, not linked from any hub, and noindex
// on both the document meta and the response header.
const UNLISTED_PREFIXES = ["/motek", "/boathouse"];
const NOINDEX_HEADER = "noindex, nofollow, noarchive";

function isUnlistedPath(pathname) {
  const p = stripTrailingSlash(pathname).toLowerCase();
  return UNLISTED_PREFIXES.some((prefix) => p === prefix || p.startsWith(`${prefix}/`));
}

// ---------------------------------------------------------------------------
// /mfg — password-gated training exam. Not in UNLISTED_PREFIXES on purpose:
// it needs its own auth branch, and it is never added to robots.txt or the
// sitemap. The dataset lives in src/mfg-data.js and never reaches public/, so
// the payload cannot be fetched without a valid session cookie.
// ---------------------------------------------------------------------------

const MFG_PREFIX = "/mfg";
const MFG_COOKIE = "mfg_session";
const MFG_SESSION_INPUT = "mfg-session-v1";
const MFG_MAX_AGE = 43200;
const MFG_COOKIE_ATTRS = "HttpOnly; Secure; SameSite=Lax; Path=/mfg";
const MFG_TEXT_ENCODER = new TextEncoder();

function isMfgPath(pathname) {
  const p = stripTrailingSlash(pathname).toLowerCase();
  return p === MFG_PREFIX || p.startsWith(`${MFG_PREFIX}/`);
}

// HMAC-SHA256 over the session input plus an expiry timestamp, keyed by the
// shared password. Signing the expiry means a copied cookie stops working when
// it times out, unlike a digest of a constant.
async function mfgSessionValue(secret, expiresAt) {
  const key = await crypto.subtle.importKey(
    "raw",
    MFG_TEXT_ENCODER.encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"]
  );
  const signature = await crypto.subtle.sign(
    "HMAC",
    key,
    MFG_TEXT_ENCODER.encode(`${MFG_SESSION_INPUT}:${expiresAt}`)
  );
  return Array.from(new Uint8Array(signature))
    .map((byte) => byte.toString(16).padStart(2, "0"))
    .join("");
}

function parseCookies(request) {
  const header = request.headers.get("Cookie") || "";
  const jar = {};
  for (const part of header.split(";")) {
    const eq = part.indexOf("=");
    if (eq < 1) continue;
    jar[part.slice(0, eq).trim()] = part.slice(eq + 1).trim();
  }
  return jar;
}

// Length-independent comparison: always walks the longer string, so the
// compare time does not leak the expected value's length.
function mfgSafeEqual(a, b) {
  if (typeof a !== "string" || typeof b !== "string") return false;
  const length = Math.max(a.length, b.length);
  let diff = a.length ^ b.length;
  for (let i = 0; i < length; i += 1) {
    diff |= (a.charCodeAt(i) || 0) ^ (b.charCodeAt(i) || 0);
  }
  return diff === 0;
}

function mfgSecret(env) {
  const secret = env && env.MFG_QUIZ_PASSWORD;
  if (typeof secret !== "string" || secret.length === 0) return "";
  return secret;
}

async function mfgIsAuthed(request, env) {
  const secret = mfgSecret(env);
  if (!secret) return false;
  const value = parseCookies(request)[MFG_COOKIE];
  if (!value) return false;
  const dot = value.indexOf(".");
  if (dot < 1) return false;
  const expiresAt = Number(value.slice(0, dot));
  const signature = value.slice(dot + 1);
  if (!Number.isFinite(expiresAt) || expiresAt * 1000 <= Date.now()) return false;
  const expected = await mfgSessionValue(secret, expiresAt);
  return mfgSafeEqual(signature, expected);
}

async function mfgSessionCookieValue(secret) {
  const expiresAt = Math.floor(Date.now() / 1000) + MFG_MAX_AGE;
  return `${expiresAt}.${await mfgSessionValue(secret, expiresAt)}`;
}

function mfgSessionCookie(value, maxAge) {
  return `${MFG_COOKIE}=${value}; ${MFG_COOKIE_ATTRS}; Max-Age=${maxAge}`;
}

function mfgExpiredCookie() {
  return `${mfgSessionCookie("", 0)}; Expires=Thu, 01 Jan 1970 00:00:00 GMT`;
}

function mfgNoStoreHeaders(extra) {
  return {
    "Cache-Control": "no-store",
    "X-Robots-Tag": NOINDEX_HEADER,
    ...extra,
  };
}

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

// The login page holds no dataset text: no dish names, no one-liners, no drop
// lines, no allergen vocabulary, no service steps. Only config metadata.
function mfgLoginPage(showError) {
  const name = escapeHtml(MFG_CONFIG.displayName);
  const subtitle = escapeHtml(MFG_CONFIG.subtitle);
  const errorNote = showError
    ? '<p class="err" role="alert">That password is not correct. Try again.</p>'
    : "";
  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow, noarchive">
<meta name="googlebot" content="noindex, nofollow, noarchive">
<meta name="referrer" content="no-referrer">
<title>${name} — Study Access</title>
<style>
  :root { --bg:#0f172a; --card:#1e293b; --border:#334155; --text:#f8fafc; --muted:#94a3b8; --accent:#eab308; --red:#ef4444; }
  * { box-sizing:border-box; font-family:-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; -webkit-tap-highlight-color:transparent; }
  body { margin:0; min-height:100vh; display:flex; align-items:center; justify-content:center; background:var(--bg); color:var(--text); padding:14px; }
  .login-card { width:100%; max-width:380px; background:var(--card); border:1px solid var(--border); border-radius:12px; padding:26px 22px; }
  .eyebrow { text-transform:uppercase; letter-spacing:0.08em; font-size:0.72rem; font-weight:700; color:var(--muted); margin:0 0 6px; }
  h1 { margin:0 0 6px; font-size:1.3rem; color:var(--accent); }
  .conf { color:var(--muted); font-size:0.85rem; line-height:1.5; margin:0 0 20px; }
  label { display:block; font-size:0.8rem; font-weight:700; color:var(--muted); margin-bottom:6px; }
  input[type=password] { width:100%; min-height:48px; padding:12px 14px; border-radius:8px; border:1px solid var(--border); background:#0f172a; color:var(--text); font-size:1rem; }
  input[type=password]:focus { outline:none; border-color:var(--accent); }
  button { width:100%; min-height:48px; margin-top:14px; padding:13px; border-radius:8px; border:1px solid var(--accent); background:var(--accent); color:#000; font-weight:700; font-size:0.95rem; cursor:pointer; }
  .err { margin:14px 0 0; padding:10px 12px; border-radius:8px; background:rgba(239,68,68,0.18); border-left:4px solid var(--red); color:#fecaca; font-size:0.85rem; }
  .tiny-note { color:var(--muted); font-size:0.75rem; text-align:center; margin:18px 0 0; }
</style>
</head>
<body>
<main class="login-card">
  <p class="eyebrow">${subtitle}</p>
  <h1>${name}</h1>
  <p class="conf">Private study aid. Enter the team password to open the menu database, the quiz, and the service steps.</p>
  <form method="post" action="/mfg/login">
    <label for="password">Password</label>
    <input id="password" name="password" type="password" autocomplete="current-password" required autofocus>
    <button type="submit">Unlock</button>
  </form>
  ${errorNote}
  <p class="tiny-note">Unlisted. Not indexed. Not linked from the site.</p>
</main>
</body>
</html>`;
}

async function mfgFetchAsset(request, env, pathname) {
  const assetUrl = new URL(request.url);
  assetUrl.pathname = pathname;
  return env.ASSETS.fetch(new Request(assetUrl, request));
}

async function handleMfg(request, env) {
  const url = new URL(request.url);
  const pathname = stripTrailingSlash(url.pathname).toLowerCase();
  const method = request.method.toUpperCase();
  const wantsJson = pathname === `${MFG_PREFIX}/data.json`;

  // Reject a form POST that a browser sends from another site. Some browsers
  // send "Origin: null" (privacy modes, sandboxed contexts), so only a header
  // that parses to a different host is rejected; Referer is the fallback.
  if (method === "POST") {
    const sourceHost = (value) => {
      if (!value || value === "null") return "";
      try {
        return new URL(value).host;
      } catch {
        return "";
      }
    };
    const originHost = sourceHost(request.headers.get("Origin"));
    const refererHost = sourceHost(request.headers.get("Referer"));
    const claimed = originHost || refererHost;
    if (claimed && claimed !== url.host) {
      return new Response("Forbidden", {
        status: 403,
        headers: mfgNoStoreHeaders({ "Content-Type": "text/plain; charset=utf-8" }),
      });
    }
  }

  if (method === "POST" && pathname === `${MFG_PREFIX}/login`) {
    let password = "";
    try {
      const form = await request.formData();
      const field = form.get("password");
      if (typeof field === "string") password = field;
    } catch {
      password = "";
    }
    const secret = mfgSecret(env);
    if (secret && password.length > 0 && mfgSafeEqual(password, secret)) {
      const session = await mfgSessionCookieValue(secret);
      return new Response(null, {
        status: 303,
        headers: mfgNoStoreHeaders({
          Location: "/mfg",
          "Set-Cookie": mfgSessionCookie(session, MFG_MAX_AGE),
        }),
      });
    }
    return new Response(null, {
      status: 303,
      headers: mfgNoStoreHeaders({ Location: "/mfg?error=1" }),
    });
  }

  if (method === "POST" && pathname === `${MFG_PREFIX}/logout`) {
    return new Response(null, {
      status: 303,
      headers: mfgNoStoreHeaders({
        Location: "/mfg",
        "Set-Cookie": mfgExpiredCookie(),
      }),
    });
  }

  if (method === "GET" && wantsJson) {
    if (!(await mfgIsAuthed(request, env))) {
      return new Response(JSON.stringify({ error: "locked" }), {
        status: 401,
        headers: mfgNoStoreHeaders({
          "Content-Type": "application/json; charset=utf-8",
        }),
      });
    }
    const payload = {
      config: MFG_CONFIG,
      sections: MFG_SECTIONS,
      allergens: MFG_ALLERGENS,
      steps: MFG_STEPS,
      dishes: MFG_DISHES,
    };
    return new Response(JSON.stringify(payload), {
      status: 200,
      headers: mfgNoStoreHeaders({
        "Content-Type": "application/json; charset=utf-8",
      }),
    });
  }

  if (method === "GET" && pathname === MFG_PREFIX) {
    if (await mfgIsAuthed(request, env)) {
      // The asset path needs the trailing slash: assets 307s "/dir/index.html".
      const page = await mfgFetchAsset(request, env, `${MFG_PREFIX}/`);
      const out = withSecurityHeaders(page);
      out.headers.set("X-Robots-Tag", NOINDEX_HEADER);
      out.headers.set("Cache-Control", "no-store");
      return out;
    }
    const showError = new URL(request.url).searchParams.get("error") === "1";
    return new Response(mfgLoginPage(showError), {
      status: 200,
      headers: mfgNoStoreHeaders({ "Content-Type": "text/html; charset=utf-8" }),
    });
  }

  // Any other /mfg/* path: hidden behind the gate too.
  if (!(await mfgIsAuthed(request, env))) {
    return new Response("Not Found", {
      status: 404,
      headers: mfgNoStoreHeaders({ "Content-Type": "text/plain; charset=utf-8" }),
    });
  }

  const asset = await mfgFetchAsset(request, env, new URL(request.url).pathname);
  const out = withSecurityHeaders(asset);
  out.headers.set("X-Robots-Tag", NOINDEX_HEADER);
  return out;
}

function withSecurityHeaders(response) {
  const out = new Response(response.body, response);
  for (const [key, value] of Object.entries(SECURITY_HEADERS)) {
    out.headers.set(key, value);
  }
  return out;
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const { hostname, pathname } = url;

    // Always land on HTTPS before any other hop (zone Always Use HTTPS
    // should also be on; this is belt-and-suspenders).
    if (url.protocol === "http:") {
      url.protocol = "https:";
      return Response.redirect(url.toString(), 301);
    }

    // www is not canonical: 301 to the apex, same path + query.
    if (hostname === WWW_HOST) {
      return Response.redirect(
        `https://${APEX_HOST}${pathname}${url.search}`,
        301
      );
    }

    // Publication surfaces keep living on Substack: 301, same path + query.
    if (isSubstackPath(pathname)) {
      return Response.redirect(`${SUBSTACK_BASE}${pathname}${url.search}`, 301);
    }

    // Retired hubs: LP bot / harness → home. CXW/GEO slot became SPCX/Anthropic.
    const retired = stripTrailingSlash(pathname);
    if (
      retired === "/prediction-market-lp-bot" ||
      retired === "/agent-harness"
    ) {
      return Response.redirect(`https://${APEX_HOST}/${url.search}`, 301);
    }
    if (retired === "/cxw-geo") {
      return Response.redirect(
        `https://${APEX_HOST}/spcx-anthropic/${url.search}`,
        301
      );
    }

    // Password-gated training exam. The gate runs before the assets binding
    // for every /mfg path, so the payload never leaves the worker unauthenticated.
    if (isMfgPath(pathname)) {
      return handleMfg(request, env);
    }

    // Unlisted app: serve /motek directly, without a trailing-slash hop, and
    // stamp noindex on the response as well as in the document head.
    // The asset path needs the trailing slash: assets 307s "/dir/index.html".
    if (isUnlistedPath(pathname)) {
      // Only the bare page path is rewritten to its directory. Sub-assets such
      // as /boathouse/boathouse-data.js must reach the assets binding as-is,
      // otherwise they resolve to /boathouse/<file>/ and 404.
      const root = stripTrailingSlash(pathname);
      const isPage = UNLISTED_PREFIXES.includes(root.toLowerCase());
      const assetUrl = new URL(request.url);
      if (isPage) assetUrl.pathname = `${root}/`;
      const unlisted = await env.ASSETS.fetch(
        isPage ? new Request(assetUrl, request) : request
      );
      const out = withSecurityHeaders(unlisted);
      out.headers.set("X-Robots-Tag", NOINDEX_HEADER);
      return out;
    }

    // Everything else: serve owned static assets. Unknown paths use
    // public/404.html via assets.not_found_handling = "404-page".
    // Headers are set here because run_worker_first skips public/_headers.
    const assetResponse = await env.ASSETS.fetch(request);
    return withSecurityHeaders(assetResponse);
  },
};
