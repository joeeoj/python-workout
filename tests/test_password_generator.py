import string

import pytest

from functions.password_generator import create_password_generator


def test_length():
    func = create_password_generator('abcdefghijklmnopqrstuvwxyz')
    assert len(func(10)) == 10

def test_subset():
    func = create_password_generator('ABCDEFJHIJKL')
    assert set(func(5)).issubset(string.ascii_uppercase)
