"""Removed types because they weren't working with mypy."""
def firstlast(seq):
    """exercise 9 -- should work with str, list, or tuple"""
    return seq[:1] + seq[-1:]
