# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A small sample of a coding agent built on the Strands Agents SDK (`strands-agents`). It is a single-file app (`src/main.py`) that creates an `Agent` with the vended tools `file_editor` and `shell`. There is no test suite, and `README.md` is empty.

## Commands

Python 3.14+ and [uv](https://docs.astral.sh/uv/) are required. The scripts in `scripts/` unset `VIRTUAL_ENV` and run through `uv`.

- Run the app: `scripts/run.sh` (arguments are passed through to `src/main.py`)
- Lint and format check, without modifying files: `scripts/lint.sh`
- Auto-fix and format (includes import sorting): `scripts/format.sh`

Ruff is configured in `pyproject.toml`: line length 88, rules `E, F, I, UP, B`, double quotes.

## Architecture notes

- `src/main.py` defines a `BedrockModel` (`jp.amazon.nova-2-lite-v1:0`) as `bedrock_model`, but `Agent(tools=[file_editor, shell])` is constructed **without** `model=bedrock_model`. The agent therefore uses the SDK's default Bedrock model, and `bedrock_model` is currently unused. Pass `model=bedrock_model` to use the Nova model.
- Running the agent needs AWS credentials and Bedrock access in the configured region.
- `shell` and `file_editor` execute commands and edit files on the local machine when the agent runs.
