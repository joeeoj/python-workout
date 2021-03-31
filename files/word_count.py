from typing import Tuple


"""Splits counting and printing to make testing easier"""
def wordcount(fname: str) -> Tuple[int, int, int, int]:
    chars, words, lines, unique_words = 0, 0, 0, set()
    with open(fname) as f:
        for row in f.readlines():
            chars += len(row)
            words += len(row.split())
            lines += 1
            unique_words.update(set(row.split()))
    return chars, words, lines, len(unique_words)

def wc(chars: int, words: int, lines: int, unique_words: int) -> None:
    print(f'{lines:>8}{words:>8}{chars:>8}{unique_words:>8}')
