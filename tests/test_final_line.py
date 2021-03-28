from pathlib import Path

import pytest

from files.final_line import get_final_line


DATA_DIR = Path(__file__).parent / 'test_data'


def test_lyrics():
    fname = DATA_DIR / 'lyrics.txt'
    assert get_final_line(fname).strip() == 'Somewhere lost in space'

def test_empty():
    fname = DATA_DIR / 'empty.txt'
    assert get_final_line(fname) == ''
