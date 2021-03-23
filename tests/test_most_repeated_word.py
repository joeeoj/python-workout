import pytest

from lists_and_tuples.most_repeated_word import repeated_word
from lists_and_tuples.most_repeated_word import repeated_word_alt


def test_example():
    assert repeated_word(['this', 'is', 'an', 'elementary', 'test', 'example']) == 'elementary'

def test_example_alt():
    assert repeated_word_alt(['this', 'is', 'an', 'elementary', 'test', 'example']) == 'elementary'
