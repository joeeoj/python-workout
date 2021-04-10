#!/bin/bash
# helper for flake8, mypy, and pytest
# also a pre-commit hook and a github actions but good to run yourself pre-commit, if you remember

# linter
flake8

# type hinting
mypy . --exclude tests

# tests
pytest
