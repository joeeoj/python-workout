import pytest

from modules_and_packages.freedonia import calculate_tax


def test_example():
    """This test simulates the use_freedonia.py part of the workout"""
    assert calculate_tax(500, 'Harpo', 12) == 625

def test_invalid_province_no_taxes():
    assert calculate_tax(100, 'Murica', 23) == 100

def test_rounding():
    # would be 111.94583333333333 without rounding
    assert calculate_tax(67, 'Groucho', 23) == 111.95
