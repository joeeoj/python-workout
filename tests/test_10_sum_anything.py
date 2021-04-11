import pytest

from lists_and_tuples.sum_anything import mysum


def test_int():
    assert mysum(1, 2, 3, 4, 5) == 15

def test_float():
    assert mysum(2.0, 4.0, 6.0) == 12.0

def test_list():
    assert mysum([1, 2], [3, 4], [5, 6]) == [1, 2, 3, 4, 5, 6]
