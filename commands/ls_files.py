import os
from argparse import Namespace

from util import read_index


def cmd_ls_files(args: Namespace) -> str:
    result: str = ""
    for entry in read_index(os.getcwd()):
        line = f"{entry.sha1.hex()} {entry.path}\n"
        result += line
        print(line)
    return result
