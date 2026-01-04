import json
import logging
import os
from pathlib import Path

from bedrock_agentcore.memory import MemoryClient

REGION = os.environ.get("AWS_REGION", "us-west-2")
CONFIG_PATH = Path(__file__).with_name(".agentcore_memory.json")

client = MemoryClient(region_name=REGION)
logging.getLogger("bedrock_agentcore.memory").setLevel(logging.WARNING)
mem = client.create_or_get_memory(
    name="MyAgentMemory",
    description="Memory for Strands agent (STM)",
)
memory_id = mem.get("memoryId", mem.get("id"))

CONFIG_PATH.write_text(
    json.dumps(
        {
            "memory_id": memory_id,
            "region": REGION,
        },
        ensure_ascii=True,
        indent=2,
    )
    + "\n",
    encoding="utf-8",
)

print(memory_id)
print(f"Saved config: {CONFIG_PATH}")
