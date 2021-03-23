import pytest

from lists_and_tuples.alphabetizing_names import alphabetize_names


def test_example():
    people = [
        {'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
        {'first':'Donald', 'last':'Trump', 'email':'president@whitehouse.gov'},
        {'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.ru'},
    ]
    sorted_people = [
        {'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
        {'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.ru'},
        {'first':'Donald', 'last':'Trump', 'email':'president@whitehouse.gov'},
    ]
    assert alphabetize_names(people) == sorted_people

def test_random_names():
    people = [
        {'first':'Kevin', 'last':'Reeves', 'email':'reeves.k@example.com'},
        {'first':'Aaron', 'last':'Kelly', 'email':'aaron.kelly@example.com'},
        {'first':'Mae', 'last':'Maxwell', 'email':'m.maxwell@example.com'},
    ]
    sorted_people = [
        {'first':'Aaron', 'last':'Kelly', 'email':'aaron.kelly@example.com'},
        {'first':'Mae', 'last':'Maxwell', 'email':'m.maxwell@example.com'},
        {'first':'Kevin', 'last':'Reeves', 'email':'reeves.k@example.com'},
    ]
    assert alphabetize_names(people) == sorted_people
