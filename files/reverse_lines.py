def reverse_lines(fname: str, fout: str) -> None:
    # cool to know you can do this on a single line instead of nested with statements
    with open(fname) as f, open(fout, 'wt') as fo:
        for line in f.readlines():
            # remove trailing newline, reverse, then add back
            fo.write(line.rstrip()[::-1] + '\n')
