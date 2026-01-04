import json
import os
from pathlib import Path

from strands import Agent
from bedrock_agentcore.memory.integrations.strands.config import AgentCoreMemoryConfig
from bedrock_agentcore.memory.integrations.strands.session_manager import AgentCoreMemorySessionManager

CONFIG_PATH = Path(__file__).with_name(".agentcore_memory.json")
_config = {}
if CONFIG_PATH.exists():
    _config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))

MEMORY_ID = os.environ.get("AGENTCORE_MEMORY_ID", _config.get("memory_id"))
REGION = os.environ.get("AWS_REGION", _config.get("region", "us-west-2"))


def build_agent(actor_id: str, session_id: str) -> Agent:
    if not MEMORY_ID:
        raise RuntimeError(
            "Missing memory id. Run create_memory.py or set AGENTCORE_MEMORY_ID."
        )
    config = AgentCoreMemoryConfig(
        memory_id=MEMORY_ID,
        actor_id=actor_id,
        session_id=session_id,
    )

    session_manager = AgentCoreMemorySessionManager(
        agentcore_memory_config=config,
        region_name=REGION,
    )

    return Agent(
        system_prompt="You are a helpful assistant. Use short-term memory within the session.",
        session_manager=session_manager,
        callback_handler=None,
    )


def run_cli() -> None:
    actor_id = os.environ.get("AGENTCORE_ACTOR_ID", "user-1")
    session_id = os.environ.get("AGENTCORE_SESSION_ID", "session-1")
    agent = build_agent(actor_id=actor_id, session_id=session_id)
    print("Type a message and press Enter. Type 'exit' to quit.")
    while True:
        try:
            user_input = input("> ").strip()
        except EOFError:
            break
        if not user_input:
            continue
        if user_input.lower() in {"exit", "quit"}:
            break
        response = agent(user_input)
        print(response)


if __name__ == "__main__":
    run_cli()
