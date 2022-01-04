import argparse


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Reinvention of git in python")
    subparsers = parser.add_subparsers(title="Commands", dest="command")
    # subparsers.required = True

    # write parse algorithm here
    # init
    init_parser = subparsers.add_parser("init")
    init_parser.add_argument("directory", type=str, default=".", nargs="?")
    # hash-object
    hash_parser = subparsers.add_parser("hash-object")
    hash_parser.add_argument("path", type=str)
    # cat-file
    cat_parser = subparsers.add_parser("cat-file")
    cat_parser.add_argument("hash_value", type=str)
    # ls-files
    ls_parser = subparsers.add_parser("ls-files")  # noqa
    # add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("files", type=str, nargs="+")
    # write-tree
    write_tree_parser = subparsers.add_parser("write-tree")  # noqa
    # commit
    commit_parser = subparsers.add_parser("commit")
    commit_parser.add_argument("--message", "-m", type=str)
    commit_parser.add_argument("--author", type=str, default="anonymous", nargs="?")
    # rebase
    rebase_parser = subparsers.add_parser("rebase")
    rebase_parser.add_argument("-i", "--interactive", action="store_true")

    return parser


def get_options() -> argparse.Namespace:
    return get_parser().parse_args()
