from typing import Any, List


def flatten(items: List[List[Any]]) -> List[Any]:
    return [row for item in items for row in item]
