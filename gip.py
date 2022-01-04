from argparse import Namespace

from commands import cmd_add, cmd_cat_file, cmd_hash_object, cmd_init
from options import get_options


def main(args: Namespace) -> None:
    if args.command == "init":
        cmd_init(args)
    elif args.command == "hash-object":
        cmd_hash_object(args)
    elif args.command == "cat-file":
        cmd_cat_file(args)
    elif args.command == "add":
        cmd_add(args)
    elif args.command == "commit":
        raise NotImplementedError


if __name__ == "__main__":
    args = get_options()
    main(args)
