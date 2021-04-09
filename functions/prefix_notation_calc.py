import operator
from typing import Optional, Union


OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    'x': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '**': operator.pow,
}


def calc(expression: str) -> Optional[Union[int, float]]:
    op, a, b = expression.split()
    func = OPERATORS.get(op)
    if func is not None:
        return func(int(a), int(b))
    return None
