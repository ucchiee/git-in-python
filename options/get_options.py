import argparse


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Reinvention of git in python")
    subparsers = parser.add_subparsers(title="Commands", dest="command")
    # subparsers.required = True

    # write parse algorithm
    # init
    init_parser = subparsers.add_parser("init")
    init_parser.add_argument("directory", type=str, default=".", nargs="?")
    # rebase
    rebase_parser = subparsers.add_parser("rebase")
    rebase_parser.add_argument("-i", "--interactive", action="store_true")

    return parser


def get_options() -> argparse.Namespace:
    return get_parser().parse_args()
