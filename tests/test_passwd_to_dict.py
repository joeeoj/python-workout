from pathlib import Path

import pytest

from files.passwd_to_dict import passwd_to_dict


DATA_DIR = Path(__file__).parent / 'test_data'


def test_example():
    """Example includes a comment line that should be skipped."""
    ans = {
        'nobody': -2,
        'root': 0,
        'daemon': 1,
    }
    assert passwd_to_dict(DATA_DIR / 'passwd') == ans
