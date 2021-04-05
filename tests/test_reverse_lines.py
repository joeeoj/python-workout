from pathlib import Path

import pytest

from files.reverse_lines import reverse_lines


DATA_DIR = Path(__file__).parent / 'test_data'


def test_example(tmp_path):
    fname = DATA_DIR / 'reverse.txt'
    fout = tmp_path / 'reverse_lines_test.txt'

    reverse_lines(fname, fout)

    result = ("fed cba\n"
              "lkj ihg\n")

    assert fout.read_text() == result
