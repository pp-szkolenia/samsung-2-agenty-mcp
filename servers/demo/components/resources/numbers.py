import json
from pathlib import Path

from fastmcp.resources import resource

NUMBERS_PATH = Path(__file__).parent / "numbers.json"


@resource("demo://numbers", mime_type="application/json")
def numbers() -> list[dict[str, int]]:
    """List of number pairs (keys A and B) to be processed with the operation_a tool."""
    return json.loads(NUMBERS_PATH.read_text(encoding="utf-8"))
