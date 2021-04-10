def sum_numbers(inputs: str) -> int:
    """Works with negative numbers"""
    return sum([int(s) for s in inputs.split() if s.lstrip('-').isdigit()])
