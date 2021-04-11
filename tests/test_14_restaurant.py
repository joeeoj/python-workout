from io import StringIO

import pytest

from dicts_and_sets.restaurant import restaurant


def test_example(monkeypatch, capfd):
    """https://gist.github.com/GenevieveBuckley/efd16862de9e2fe7adfd2bf2bef93e02"""
    user_inputs = StringIO("tea\n"
                           "sandwich\n"
                           "\n")
    monkeypatch.setattr('sys.stdin', user_inputs)

    restaurant()
    out, err = capfd.readouterr()

    assert out == ("What is your order? tea costs 3, your total is 3\n"
                   "What is your order? sandwich costs 10, your total is 13\n"
                   "What is your order? Your total is 13\n")


def test_zero(monkeypatch, capfd):
    user_inputs = StringIO("\n")
    monkeypatch.setattr('sys.stdin', user_inputs)

    restaurant()
    out, err = capfd.readouterr()

    assert out == ("What is your order? Your total is 0\n")
