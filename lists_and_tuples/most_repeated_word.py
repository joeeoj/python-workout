from collections import Counter
from typing import Optional, List


def repeated_word(words: List[str]) -> Optional[str]:
    """exercise 12 -- Return the string that contains the greatest number of repeated letters"""
    max_count, ans = 0, None
    for word in words:
        word_count = Counter(word).most_common(1)[0][1]
        if word_count > max_count:
            max_count, ans = word_count, word
    return ans

def most_repeated_letter(word: str) -> int:
    return Counter(word).most_common(1)[0][1]

def repeated_word_alt(words: List[str]) -> str:
    """alt solution with separate 'key' function per the book. Definitely cleaner."""
    return max(words, key=most_repeated_letter)
