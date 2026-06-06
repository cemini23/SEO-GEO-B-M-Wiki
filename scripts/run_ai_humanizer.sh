#!/usr/bin/env bash
# Launch AI Text Humanizer Streamlit UI (local-only, optional tool).
# Venv: ~/.cemini/venvs/ai-text-humanizer (repo path contains ':' — venv lives outside)
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
APP_DIR="$ROOT/tools/ai-text-humanizer"
# Repo folder name contains ':' — venv cannot live inside it; use ~/.cemini/venvs
VENV="${AI_HUMANIZER_VENV:-$HOME/.cemini/venvs/ai-text-humanizer}"

if [[ ! -d "$APP_DIR" ]]; then
  echo "Cloning AI-Text-Humanizer-App into tools/ai-text-humanizer ..."
  git clone --depth 1 https://github.com/DadaNanjesha/AI-Text-Humanizer-App.git "$APP_DIR"
fi

if [[ ! -d "$VENV" ]]; then
  echo "Creating venv and installing deps (first run may take 2–3 min) ..."
  python3 -m venv "$VENV"
  "$VENV/bin/pip" install -q --upgrade pip
  "$VENV/bin/pip" install -q spacy nltk sentence-transformers streamlit
  "$VENV/bin/python" -m spacy download en_core_web_sm
fi

cd "$APP_DIR"
exec "$VENV/bin/streamlit" run main.py --server.headless true
