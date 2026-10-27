"""Minimal demo MCP server exposed over streamable HTTP."""

from fastmcp import FastMCP

mcp = FastMCP("demo")


@mcp.tool
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


@mcp.tool
def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


@mcp.resource("demo://about")
def about() -> str:
    """Short description of this server."""
    return "Demo MCP server built with FastMCP."


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
