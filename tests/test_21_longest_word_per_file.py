from pathlib import Path

import pytest

from files.longest_word_per_file import find_longest_word, find_all_longest_words


DATA_DIR = Path(__file__).parent / 'test_data'


def test_example():
    fname = DATA_DIR / 'longword.txt'
    assert find_longest_word(fname) == 'floccinaucinihilipilification'

def test_books():
    book_dir = DATA_DIR / 'books'

    ans = {
        'moby_dick_or_the_whale.txt': 'uninterpenetratingly',
        'pride_and_prejudice.txt': 'disinterestedness',
        'little_women.txt': 'philoprogenitiveness',
    }

    assert find_all_longest_words(book_dir) == ans
