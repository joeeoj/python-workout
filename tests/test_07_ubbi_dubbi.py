import pytest

from strings.ubbi_dubbi import ubbi_dubbi


def test_milk():
    assert ubbi_dubbi('milk') == 'mubilk'

def test_program():
    assert ubbi_dubbi('program') == 'prubogrubam'
