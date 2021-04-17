import string
from typing import List


GEMATRIA = {s: i for s, i in zip(string.ascii_lowercase, range(1, 27))}


def gematria_for(word: str) -> int:
    return sum(GEMATRIA.get(c, 0) for c in word)

def gematria_equal_words(word: str, fname: str) -> List[str]:
    """Given a word and path of a word list, returns list of all words from the list with the same gematria value as the
    given word"""
    result = []
    target = gematria_for(word)
    with open(fname) as f:
        for line in f:
            if gematria_for(line) == target:
                result.append(line.strip())
    return result
