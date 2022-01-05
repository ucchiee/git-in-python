import os
from argparse import Namespace

from util import write_tree


def cmd_write_tree(args: Namespace) -> str:
    hash = write_tree(os.getcwd())
    print(hash)
    return hash
