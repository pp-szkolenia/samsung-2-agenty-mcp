from fastmcp.prompts import prompt


@prompt
def operation_a_pairs(request: str) -> str:
    """Apply operation A to pairs from the numbers resource, per the user's request."""
    return f"""\
User request: {request}

Task: apply the custom "operation A" (A * B + (A - B), not ordinary addition) to
pairs of numbers from the resource demo://numbers, a JSON list of objects with
numeric keys "A" and "B".

Indexing: pairs are indexed from 0 and an ordinal is the index itself
("zeroth" = 0, "first" = 1, "second" = 2, ...). So "the second pair" is the
object at index 2, i.e. the third one in the list. If the index is out of range,
say how many pairs exist instead of guessing.

Procedure:
1. Read demo://numbers and find the requested pair(s).
2. Call the operation_a tool with a=A and b=B. Never compute the result yourself.
3. Answer with the index, the pair and the result, e.g.
   "Pair at index 2: A=-4, B=12, operation A = -64".
"""
