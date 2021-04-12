from strings.pig_latin import pig_latin


def plfile(fname: str) -> str:
    result = ''
    with open(fname) as f:
        for line in f.readlines():
            result += ' '.join((pig_latin(word) for word in line.split()))
    return result
