import pytest

from dicts_and_sets.how_many_diff_nums import how_many_different_numbers


def test_example():
    assert how_many_different_numbers([1, 2, 3, 1, 2, 3, 4, 1]) == 4

def test_another_example():
    assert how_many_different_numbers([1, 1, 1, 1, 2, 2, 2]) == 2

def test_empty_list():
    assert how_many_different_numbers([]) == 0
