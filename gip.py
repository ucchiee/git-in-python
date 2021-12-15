from argparse import Namespace
import os

from options import get_options
from commands import cmd_init, cmd_hash_object


def main(args: Namespace) -> None:
    if args.command == "init":
        args.directory = os.path.abspath(args.directory)
        cmd_init(args)
    elif args.command == "hash-object":
        cmd_hash_object(args)


if __name__ == "__main__":
    args = get_options()
    main(args)
