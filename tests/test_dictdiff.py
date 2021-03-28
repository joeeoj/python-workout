import pytest

from dicts_and_sets.dictdiff import dictdiff


def test_empty_result():
    d1 = {'a':1, 'b':2, 'c': 3}
    d2 = {'a':1, 'b':2, 'c': 3}
    assert dictdiff(d1, d2) == {}

def test_first_example():
    d3 = {'a':1, 'b':2, 'd':3}
    d4 = {'a':1, 'b':2, 'c':4}
    assert dictdiff(d3, d4) == {'d': [3, None], 'c': [None, 4]}

def test_second_example():
    d1 = {'a':1, 'b':2, 'c': 3}
    d5 = {'a':1, 'b':2, 'd':4}
    assert dictdiff(d1, d5) == {'c': [3, None], 'd': [None, 4]}
