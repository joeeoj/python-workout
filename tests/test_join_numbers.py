import pytest

from comprehension.join_numbers import join_numbers


def test_example():
    assert join_numbers(range(15)) == '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14'

def test_example_with_negative():
    assert join_numbers(range(-10,5)) == '-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4'
