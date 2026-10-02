#!/usr/bin/env bash
# Ruffで自動修正（import整理を含む）とフォーマットを行う
set -euo pipefail
cd "$(dirname "$0")/.."
unset VIRTUAL_ENV

uv run ruff check --fix .
uv run ruff format .
