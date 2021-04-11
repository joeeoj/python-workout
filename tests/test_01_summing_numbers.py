import pytest

from numeric_types.summing_numbers import mysum


def test_add():
    assert mysum(5, 5, 5) == 15

def test_negative():
    assert mysum(5, -10) == -5

def test_many():
    assert mysum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == 55
