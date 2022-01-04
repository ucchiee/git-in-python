import os
from argparse import Namespace

from util import detect_dot_git, hash_object


def cmd_hash_object(args: Namespace) -> str:
    path: str = os.path.abspath(args.path)

    # check path
    if not os.path.exists(path):
        print(f"{path} does not exists")
        return ""

    # check repo
    dot_git_dir = detect_dot_git(path)
    if not dot_git_dir:
        print("there is not a git repository")
        return ""

    sha1_hash = hash_object(path)
    print(sha1_hash)
    return sha1_hash


def main():
    pass


if __name__ == "__main__":
    main()
