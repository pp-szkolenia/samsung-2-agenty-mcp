"""Minimal demo MCP server exposed over streamable HTTP.

Tools, resources and prompts are discovered from the ``components`` directory.
"""

from pathlib import Path

from fastmcp import FastMCP
from fastmcp.server.providers import FileSystemProvider

mcp = FastMCP(
    "demo",
    providers=[FileSystemProvider(Path(__file__).parent / "components")],
)


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
