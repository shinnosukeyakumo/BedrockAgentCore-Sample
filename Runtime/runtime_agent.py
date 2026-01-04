from typing import Any, Dict

from strands import Agent
from bedrock_agentcore.runtime import BedrockAgentCoreApp

agent = Agent(system_prompt="You are a helpful assistant.")
app = BedrockAgentCoreApp()


@app.entrypoint
def invoke(payload: Dict[str, Any]) -> str:
    user_message = payload.get("prompt", "")
    response = agent(user_message)
    return str(response)


if __name__ == "__main__":
    app.run()
