def dictdiff(a: dict, b: dict) -> dict:
    """Returns the different between two dicts"""
    d = {}
    keys = a.keys() | b.keys()  # dict_keys subclasses the set union operator

    for k in keys:
        a_val, b_val = a.get(k), b.get(k)
        if a_val is None or b_val is None or a_val != b_val:
            d[k] = [a_val, b_val]
    return d
