from pathlib import Path

import pytest

from files.reading_writing_csvs import passwd_to_csv


DATA_DIR = Path(__file__).parent / 'test_data'


def test_example(tmp_path):
    fname = DATA_DIR / 'passwd2'
    fout = tmp_path / 'reading_writing_csv_test.csv'

    passwd_to_csv(fname, fout)

    result = ("root\t0\n"
              "daemon\t1\n"
              "_ftp\t98\n")

    assert fout.read_text() == result

def test_old_passwd_file(tmp_path):
    fname = DATA_DIR / 'passwd'
    fout = tmp_path / 'reading_writing_csv_test.csv'

    passwd_to_csv(fname, fout)

    result = ("nobody\t-2\n"
              "root\t0\n"
              "daemon\t1\n")

    assert fout.read_text() == result
