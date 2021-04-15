from typing import Set


VOWELS = {'a', 'e', 'i', 'o', 'u'}
VOWELS_LIST = sorted(list(VOWELS))


def supervocalic(word: str) -> bool:
    """word that contains all 5 vowels in (a,e,i,o,u), each appears once, and are in alphabetical order"""
    idx = 0
    for c in word:
        if c in VOWELS:
            if idx < len(VOWELS_LIST) and c == VOWELS_LIST[idx]:
                idx += 1
            else:
                return False
    if idx != 5:
        return False
    return True

def get_sv(fname: str) -> Set[str]:
    results = set()
    with open(fname) as f:
        for line in f.readlines():
            for word in line.split():
                if supervocalic(word):
                    results.update([word])
    return results
