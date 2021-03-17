def pig_latin(s: str) -> str:
    if s[0] in 'aeiou':
        return s + 'way'
    return s[1:] + s[0] + 'ay'
