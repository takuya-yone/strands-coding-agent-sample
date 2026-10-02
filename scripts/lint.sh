#!/usr/bin/env bash
# Ruffでlintとフォーマットチェックを行う（ファイルは変更しない）
set -euo pipefail
cd "$(dirname "$0")/.."
unset VIRTUAL_ENV

uv run ruff check .
uv run ruff format --check .
