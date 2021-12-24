from argparse import Namespace

from commands import cmd_init, cmd_hash_object
from options import get_options


def main(args: Namespace) -> None:
    if args.command == "init":
        cmd_init(args)
    elif args.command == "hash-object":
        cmd_hash_object(args)


if __name__ == "__main__":
    args = get_options()
    main(args)
