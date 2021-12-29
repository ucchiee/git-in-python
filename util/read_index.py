import os
import struct
from hashlib import sha1

from classes import IndexEntry
from util.detect_dot_git import detect_dot_git


def read_index(top_dir: str, print_error: bool = False) -> list[IndexEntry]:
    dot_git_dir: str = detect_dot_git(top_dir)
    if not dot_git_dir:
        if print_error:
            print("Not in a git repository")
        return []

    index_path: str = os.path.join(dot_git_dir, "index")
    if not os.path.exists(index_path):
        if print_error:
            print("there is not a index file yet")
        return []

    with open(index_path, mode="rb") as f:
        index_data: bytes = f.read()

    checksum: bytes = sha1(index_data[:-20]).digest()
    if checksum != index_data[-20:]:
        if print_error:
            print("invalid index")
        return []

    signature, version, num_entries = struct.unpack("!4sLL", index_data)
    index_data = index_data[12:-20]
    if signature != b"DIRC":
        if print_error:
            print("invalid signature, must be DIRC")
        return []
    if version != 2:
        if print_error:
            print("invalid version, must be 2")
        return []

    raise NotImplementedError
    return []


if __name__ == "__main__":
    pass
