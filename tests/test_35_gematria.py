from pathlib import Path

import pytest

from comprehension.gematria import gematria_for
from comprehension.gematria import gematria_equal_words


DATA_DIR = Path(__file__).parent / 'test_data'


def test_simple():
    assert gematria_for('dad') == 9

def test_capitalization_ignored():
    assert gematria_for('Dad') == 5

def test_symbols_ignored():
    assert gematria_for('#*&%#*&$') == 0

def test_numbers_ignored():
    assert gematria_for('129382') == 0

def test_long_word_equal():
    fname = DATA_DIR / 'words_full.txt'
    expected = ['counterinterpretation', 'deanthropomorphization', 'formaldehydesulphoxylic']

    assert gematria_equal_words('floccinaucinihilipilification', fname) == expected
