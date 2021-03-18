def ubbi_dubbi(word: str) -> str:
    """exercise 7"""
    s = ''
    for w in word:
        if w in 'aeiou':
            s += 'ub'
        s += w
    return s
