from typing import Union


def firstlast(seq: Union[str, list, tuple]):
    """exercise 9"""
    if isinstance(seq, str):
        return ''.join([seq[0], seq[-1]])
    if isinstance(seq, list):
        return [seq[0], seq[-1]]
    if isinstance(seq, tuple):
        return (seq[0], seq[-1])
    return None
