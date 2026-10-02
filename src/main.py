import os

from strands import Agent
from strands.models import BedrockModel
from strands.vended_tools import file_editor, shell

JP_NOVA_2_LITE = "jp.amazon.nova-2-lite-v1:0"
MODEL_ID = os.getenv("MODEL_ID", JP_NOVA_2_LITE)
EXIT_COMMANDS = {"exit", "quit"}

bedrock_model = BedrockModel(model_id=MODEL_ID)
agent = Agent(
    model=bedrock_model,
    tools=[file_editor, shell],
    system_prompt=(
        """
        あなたはコーディングのプロフェッショナルです。
        """
    ),
)


def main() -> None:
    print("終了するには 'exit' または 'quit' を入力してください (Ctrl+D でも終了)")
    while True:
        try:
            user_input = input("\n> ").strip()
        except EOFError, KeyboardInterrupt:
            print()
            break
        if not user_input:
            continue
        if user_input.lower() in EXIT_COMMANDS:
            break
        agent(user_input)


if __name__ == "__main__":
    main()
