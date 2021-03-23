from typing import Union


def firstlast(seq: Union[str, list, tuple]):
    """exercise 9"""
    return seq[:1] + seq[-1:]
