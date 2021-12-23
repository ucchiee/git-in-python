import os
import zlib
from argparse import Namespace
from hashlib import sha1

from util import detect_dot_git


def cmd_hash_object(args: Namespace) -> None:
    path: str = os.path.abspath(args.path)

    # check path
    if not os.path.exists(path):
        print(f"{path} does not exists")
        return

    # check repo
    dot_git_dir = detect_dot_git(path)
    if not dot_git_dir:
        print("there is not a git repository")
        return

    # hash object
    with open(path, mode="r") as f:
        content: str = f.read()
    header: str = f"blob {len(content)}\0"
    store: str = header + content
    content_zlib = zlib.compress(store.encode())
    sha1_hash: str = sha1(store.encode()).hexdigest()

    # write object
    dirname, filename = sha1_hash[:2], sha1_hash[2:]
    obj_dir: str = os.path.join(dot_git_dir, "objects", dirname)
    os.makedirs(obj_dir, exist_ok=True)
    obj_path: str = os.path.join(obj_dir, filename)
    with open(obj_path, mode="wb") as f:  # type: ignore
        f.write(content_zlib)  # type: ignore


def main():
    pass


if __name__ == "__main__":
    main()
