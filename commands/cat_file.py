from argparse import Namespace

from util import cat_file


def cmd_cat_file(args: Namespace) -> str:
    result = cat_file(args.hash_value, print_error=True)
    print(result)
    return result


def main():
    pass


if __name__ == "__main__":
    main()
