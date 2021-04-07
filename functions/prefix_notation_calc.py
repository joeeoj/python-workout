import operator
from typing import Union


OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    'x': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '**': operator.pow,
}


def calc(expression: str) -> Union[int, float]:
    op, a, b = expression.split()
    return OPERATORS.get(op)(int(a), int(b))
