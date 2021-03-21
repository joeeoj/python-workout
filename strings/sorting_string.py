def strsort(input_str: str) -> str:
    """exercise 7

    "The fact that these data structures and methods [in, sorted, split, join] are written in C, and have been around
    for many years, means they’re also highly efficient — and not worth reinventing." (page 28)
    """
    return ''.join(sorted(input_str))
