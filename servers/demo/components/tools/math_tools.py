from fastmcp.tools import tool


@tool
def operation_a(a: int, b: int) -> int:
    """Custom "unusual addition": multiply the numbers, then add their difference.

    Formula: a * b + (a - b). Example: operation_a(3, 5) = 15 + (-2) = 13.
    The operation is not commutative: operation_a(a, b) != operation_a(b, a).
    """
    return a * b + (a - b)
