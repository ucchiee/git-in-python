from argparse import Namespace

from commands import cmd_init, cmd_hash_object, cmd_cat_file
from options import get_options


def main(args: Namespace) -> None:
    if args.command == "init":
        cmd_init(args)
    elif args.command == "hash-object":
        cmd_hash_object(args)
    elif args.command == "cat-file":
        cmd_cat_file(args)
    elif args.command == "add":
        raise NotImplementedError
    elif args.command == "commit":
        raise NotImplementedError


if __name__ == "__main__":
    args = get_options()
    main(args)
