def hex_output(hex_int: int) -> int:
    """exercise 4 -- given a hex as an int, return the decimal equivalent."""
    result = 0
    for i, h in enumerate(reversed(str(hex_int))):
        result += int(h) * (16 ** i)

    return result
