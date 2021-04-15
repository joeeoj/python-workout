from pathlib import Path

import pytest

from comprehension.supervocalic_words import get_sv, supervocalic


DATA_DIR = Path(__file__).parent / 'test_data'


def test_base_case():
    assert supervocalic('aeiou') is True

def test_single_word():
    assert supervocalic('facetious') is True

def test_false_word():
    assert supervocalic('facetiousness') is False

def test_file():
    fname = DATA_DIR / 'words.txt'
    assert get_sv(fname) == set(['abstemious', 'facetious'])
