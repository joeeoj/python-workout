def mysum(*args):
    """exercise 10 -- should work with numbers, strings, lists, and tuples, but not with sets and dicts."""
    if args is not None:
        result = args[0]  # set type with first element
        for arg in args[1:]:
            result += arg
        return result
    return None
