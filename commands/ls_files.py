import os
from argparse import Namespace

from util import read_index


def cmd_ls_files(args: Namespace):
    for entry in read_index(os.getcwd()):
        print(entry.sha1.hex(), entry.path)
