from strands import Agent
from strands.models import BedrockModel
from strands.vended_tools import file_editor, shell

# Bedrock is the default, so no model object is needed.


NOVA_2_LITE = "jp.amazon.nova-2-lite-v1:0"

bedrock_model = BedrockModel(
    model_id=NOVA_2_LITE,
)


agent = Agent(tools=[file_editor, shell])


def main():
    agent("こんにちは")


if __name__ == "__main__":
    main()
