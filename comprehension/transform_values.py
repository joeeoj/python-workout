from typing import Any, Callable


def transform_values(fn: Callable[[Any], dict], d: dict) -> dict:
    return {k: fn(v) for k, v in d.items()}
