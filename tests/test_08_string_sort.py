import pytest

from strings.sorting_string import strsort


def test_abba():
    assert strsort('abba') == 'aabb'

def test_capitalization():
    assert strsort('alabamA') == 'Aaaablm'
    assert strsort('aTlAnTa') == 'ATTaaln'
