from collections import namedtuple


Password = namedtuple('Password', ['username', 'password', 'uid', 'gid', 'unknown1', 'unknown2', 'unknown3',
                                   'user_info', 'home_dir', 'shell_path'])


def passwd_to_dict(fname: str) -> dict:
    d = {}
    with open(fname) as f:
        for line in f.readlines():
            if line.startswith('#') or line.strip() == '':
                continue
            pwd = Password(*line.strip().split(':'))
            d[pwd.username] = int(pwd.uid)
    return d
