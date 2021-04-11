import pytest

from comprehension.flatten_list import flatten


def test_example():
    assert flatten([[1,2], [3,4]]) == [1, 2, 3, 4]

def test_empties():
    assert flatten([[], [1, 2, 3], []]) == [1, 2, 3]

def test_multiple_types():
    assert flatten([[1], ['two', 'three'], [3.14159], [5, 6]]) == [1, 'two', 'three', 3.14159, 5, 6]
