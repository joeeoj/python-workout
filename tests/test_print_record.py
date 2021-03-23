import pytest

from lists_and_tuples.print_record import format_sort_records


def test_example(capfd):
    """very cool pytest fixture: https://docs.pytest.org/en/stable/capture.html"""
    people = [
        ('Donald', 'Trump', 7.85),
        ('Vladimir', 'Putin', 3.626),
        ('Jinping', 'Xi', 10.603)
    ]
    ans = ("Trump      Donald      7.85\n"
           "Putin      Vladimir    3.63\n"
           "Xi         Jinping    10.60\n")

    format_sort_records(people)

    out, err = capfd.readouterr()
    assert out == ans



def test_different_example(capfd):
    people = [
        ('Michael', 'Jordan', 23),
        ('Elon', 'Musk', 3.141),
        ('Bill', 'Gates', 7.89)
    ]
    ans = ("Jordan     Michael    23.00\n"
           "Musk       Elon        3.14\n"
           "Gates      Bill        7.89\n")

    format_sort_records(people)

    out, err = capfd.readouterr()
    assert out == ans
