from pathlib import Path

import pytest

from files.json_exercise import print_scores


DATA_DIR = Path(__file__).parent / 'test_data' / 'scores'


def test_files(capfd):
    expected = f"""\
{DATA_DIR / '9a.json'}
    math min: 65, max: 100, average: 85.0
    literature min: 78, max: 98, average: 83.6
    science min: 75, max: 97, average: 86.4\n"""

    print_scores(DATA_DIR)

    out, err = capfd.readouterr()
    assert out == expected
