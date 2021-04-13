import pytest

from comprehension.flipped_dict import flipped_dict


def test_example():
    assert flipped_dict({'a': 1, 'b': 2, 'c': 3}) == {1: 'a', 2: 'b', 3: 'c'}
