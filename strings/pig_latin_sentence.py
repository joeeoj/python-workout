from . pig_latin import pig_latin


def pl_sentence(sentence: str) -> str:
    """exercise 6"""
    return ' '.join([pig_latin(s) for s in sentence.split(' ')])
