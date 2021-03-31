from pathlib import Path

import pytest

from files.word_count import wordcount, wc


DATA_DIR = Path(__file__).parent / 'test_data'


def test_example():
    assert wordcount(DATA_DIR / 'wcfile.txt') == (165, 28, 11, 20)

def test_example_print(capfd):
    wc(*wordcount(DATA_DIR / 'wcfile.txt'))

    out, err = capfd.readouterr()
    assert out == '      11      28     165      20\n'
