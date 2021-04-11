from io import StringIO

import pytest

from dicts_and_sets.rainfall import get_rainfall


def test_example(monkeypatch, capfd):
    user_inputs = StringIO("Boston\n"
                           "5\n"
                           "New York\n"
                           "7\n"
                           "Boston\n"
                           "5\n"
                           "\n")
    monkeypatch.setattr('sys.stdin', user_inputs)

    get_rainfall()
    out, err = capfd.readouterr()

    assert out == ("City: Rainfall: City: Rainfall: City: Rainfall: City: "
                   "Boston: 10\nNew York: 7\n")
