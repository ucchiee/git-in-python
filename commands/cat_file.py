import os
import glob
from argparse import Namespace

from util import detect_dot_git


def cmd_cat_file(args: Namespace) -> str:
    # can't specify obj
    if len(args.hash_value) < 4:
        print(f"fatal: Not a valid object name {args.hash_value}")
        return ""

    dot_git_dir: str = detect_dot_git(os.getcwd())
    obj_dir: str = os.path.join(dot_git_dir, "objects")

    # object is stored in f".git/objects/{hash_value[:2]}/{hash_value[2:]}"
    # hash_value doesn't need to be complete as long as we can specify unique obj
    obj_path = os.path.join(obj_dir, args.hash_value[:2], f"{args.hash_value[2:]}*")
    obj_path_list = glob.glob(obj_path)
    if len(obj_path_list) == 0:
        print(f"there is no object that starts with {args.hash_value}")
        return ""
    elif len(obj_path_list) > 1:
        print(f"can't specify unique object by {args.hash_value}")
        return ""

    with open(obj_path_list[0], mode="r") as f:
        contents = f.read()
    print(contents)
    return contents


def main():
    pass


if __name__ == "__main__":
    main()
