import pytest

from strings.pig_latin_sentence import pl_sentence


def test_book_example():
    """error in the book - it says 'estay' but should be 'esttay'"""
    assert pl_sentence('this is a test translation') == 'histay isway away esttay ranslationtay'

def test_business_jargon():
    """props to https://www.atrixnet.com/bs-generator.html"""
    assert pl_sentence('efficiently engineer turnkey services') == 'efficientlyway engineerway urnkeytay ervicessay'
