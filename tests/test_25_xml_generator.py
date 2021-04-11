import pytest

from functions.xml_generator import myxml


def test_tag():
    assert myxml('foo') == '<foo></foo>'

def test_tag_text():
    assert myxml('foo', 'bar') == '<foo>bar</foo>'

def test_tag_text_attrs():
    assert myxml('foo', 'bar', a=1, b=2, c=3) == '<foo a="1" b="2" c="3">bar</foo>'

def test_tag_no_text_with_attrs():
    assert myxml('foo', a='123', b='456') == '<foo a="123" b="456"></foo>'
