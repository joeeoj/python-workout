import pytest

from functions.prefix_notation_calc import calc


def test_add():
    assert calc('+ 2 3') == 5

def test_sub():
    assert calc('- 2 3') == -1

def test_mul():
    assert calc('* 5 5') == 25

def test_mul_alt():
    assert calc('x 5 10') == 50

def test_div():
    assert calc('/ 100 5') == 20

def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        calc('/ 10 0')

def test_div_float():
    assert calc('/ 33 2') == 16.5

def test_mod():
    assert calc('% 17 2') == 1

def test_exp():
    assert calc('** 2 2') == 4

def test_invalid_op():
    assert calc('-- 10 5') is None
