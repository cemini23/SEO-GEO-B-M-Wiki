// Outlier Weekly owned hub router (worker-first).
// Do not blanket-301 the apex. That was the 2026-08-08 SEO defect.
// Letters stay on Substack; the apex serves owned HTML via Workers assets.

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

    // Retired hubs (shipped 2026-08-30, pulled the same day): send to home.
    const retired = stripTrailingSlash(pathname);
    if (
      retired === "/prediction-market-lp-bot" ||
      retired === "/agent-harness"
    ) {
      return Response.redirect(`https://${APEX_HOST}/${url.search}`, 301);
    }

    // Everything else: serve owned static assets. Unknown paths use
    // public/404.html via assets.not_found_handling = "404-page".
    // Headers are set here because run_worker_first skips public/_headers.
    const assetResponse = await env.ASSETS.fetch(request);
    return withSecurityHeaders(assetResponse);
  },
};
