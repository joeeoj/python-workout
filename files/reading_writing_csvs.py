import csv

from . passwd_to_dict import Password


def passwd_to_csv(fname: str, fout: str) -> None:
    """takes two filenames as arguments: the first is a passwd-style file to read from,
    and the second is the name of afile in which to write the output."""
    output = []
    with open(fname) as f:
        for line in f.readlines():
            if line.startswith('#') or line.strip() == '':
                continue
            pwd = Password(*line.strip().split(':'))
            output.append(pwd)

    with open(fout, 'wt') as f:
        csvwriter = csv.writer(f, delimiter='\t')
        for pwd in output:
            csvwriter.writerow([pwd.username, pwd.uid])
