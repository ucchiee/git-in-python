import os
from argparse import Namespace

from util import cat_file


def cmd_cat_file(args: Namespace) -> str:
    # can't specify obj
    if len(args.hash_value) < 4:
        print(f"fatal: Not a valid object name {args.hash_value}")
        return ""

    result = cat_file(args.hash_value, os.getcwd())
    if not result:
        print(f"can't specify unique object by {args.hash_value}")
    print(result)
    return result


def main():
    pass


if __name__ == "__main__":
    main()
