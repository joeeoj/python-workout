import pytest

from objects.ice_cream_scoop import Scoop
from objects.ice_cream_bowl import Bowl


def test_example():
    s1 = Scoop('chocolate')
    s2 = Scoop('vanilla')
    s3 = Scoop('persimmon')

    b = Bowl()
    b.add_scoops(s1, s2)
    b.add_scoops(s3)

    assert repr(b) == 'Bowl(chocolate,vanilla,persimmon)'
