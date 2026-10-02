# strands-coding-agent-sample

[Strands Agents SDK](https://strandsagents.com/) で作成したコーディングエージェントのサンプルです。`file_editor`（ファイル編集）と `shell`（コマンド実行）の2つのツールを持つエージェントが、Amazon Bedrock 上のモデルで動作します。

## 前提条件

- Python 3.14 以上
- [uv](https://docs.astral.sh/uv/)
- AWS 認証情報の設定と、利用するリージョンでの Amazon Bedrock のモデルアクセス

## セットアップ

```bash
uv sync
```

## 実行

```bash
scripts/run.sh
```

引数は `src/main.py` にそのまま渡されます。

## 開発

| コマンド | 内容 |
| --- | --- |
| `scripts/lint.sh` | Ruff による lint とフォーマットチェック（ファイルは変更しない） |
| `scripts/format.sh` | Ruff による自動修正（import 整理を含む）とフォーマット |

## 注意

- エージェントは `shell` と `file_editor` によって、実行したマシン上でコマンド実行やファイル編集を行います。実行環境には注意してください。
- `src/main.py` では `BedrockModel`（`jp.amazon.nova-2-lite-v1:0`）を定義していますが、現状は `Agent` に渡していません。指定する場合は `Agent(model=bedrock_model, ...)` としてください。
