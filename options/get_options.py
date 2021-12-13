import argparse


def get_options():
    parser = argparse.ArgumentParser(description="Reinvention of git in python")
    subparsers = parser.add_subparsers(title="Commands", dest="command")
    # subparsers.required = True

    # write parse algorithm
    init_parser = subparsers.add_parser("rebase")
    init_parser.add_argument("-i", "--interactive", action="store_true")

    args = parser.parse_args()
    return args
