import pytest

from comprehension.add_numbers import sum_numbers


def test_example():
    assert sum_numbers('10 abc 20 de44 30 55fg 40') == 100

def test_multiple_spaces():
    assert sum_numbers('10  abc         20 de44 30 55fg 40') == 100

def test_zeros():
    assert sum_numbers('10 abc 00 000 20 de44 30 55fg 40') == 100

def test_negative():
    assert sum_numbers('10 abc -30 20 de44 30 55fg -20 40') == 50
