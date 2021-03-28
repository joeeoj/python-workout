def get_final_line(fname: str) -> str:
    """Return final line of a file (including trailing newline) or an empty string"""
    final = ''
    with open(fname) as f:
        for row in f:
            final = row
    return final
