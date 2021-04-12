from pathlib import Path

import pytest

from comprehension.pig_latin_translation import plfile


DATA_DIR = Path(__file__).parent / 'test_data'


def test_example_file():
    fname = DATA_DIR / 'pig_latin_example.txt'

    expected = 'itway isway otnay hetay riticcay howay ountscay'

    assert plfile(fname) == expected
