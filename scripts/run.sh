#!/usr/bin/env bash
# アプリケーションを起動する（引数はそのままmain.pyに渡す）
set -euo pipefail
cd "$(dirname "$0")/.."
unset VIRTUAL_ENV

uv run python src/main.py "$@"
