import pytest

from lists_and_tuples.first_last import firstlast


def test_str():
    assert firstlast('abc') == 'ac'
    assert isinstance(firstlast('abc'), str)

def test_list():
    assert firstlast([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 9]
    assert isinstance(firstlast([1, 2, 3, 4, 5, 6, 7, 8, 9]), list)

def test_tuple():
    assert firstlast(('one', 'two', 'three', 'four')) == ('one', 'four')
    assert isinstance(firstlast(('one', 'four')), tuple)

def test_set():
    assert firstlast(set([1, 2, 3])) is None
