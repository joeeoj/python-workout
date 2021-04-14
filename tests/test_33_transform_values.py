import pytest

from comprehension.transform_values import transform_values


def test_example():
    d = {'a':1, 'b':2, 'c':3}
    assert transform_values(lambda x: x*x, d) == {'a': 1, 'b': 4, 'c': 9}
