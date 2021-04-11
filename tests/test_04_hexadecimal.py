import pytest

from numeric_types.hexadecimal_output import hex_output


def test_eighty():
    assert hex_output(50) == 80

def test_hundred():
    assert hex_output(100) == 256

def test_zero():
    assert hex_output(0) == 0
