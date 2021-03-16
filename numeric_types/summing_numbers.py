def mysum(*vals: int) -> int:
    """exercise 2"""
    ans = 0
    for val in vals:
        ans += val
    return ans
