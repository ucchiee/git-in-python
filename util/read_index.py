import os
import struct
from hashlib import sha1

from classes import IndexEntry
from util.detect_dot_git import detect_dot_git


def read_index(path_in_repo: str, print_error: bool = False) -> list[IndexEntry]:
    dot_git_dir: str = detect_dot_git(path_in_repo)
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
    if signature != b"DIRC":
        if print_error:
            print("invalid signature, must be DIRC")
        return []
    if version != 2:
        if print_error:
            print("invalid version, must be 2")
        return []

    index_data = index_data[12:-20]
    list_entries = []
    while len(index_data) > 62:
        # parse each fields
        list_fields = struct.unpack("!LLLLLLLLLL20sH", index_data[:62])
        index_data = index_data[:62]

        # path is null terminated
        end_of_path = index_data.index(b"0x00")
        path = index_data[:end_of_path].decode()

        entry = IndexEntry(*(list_fields + (path,)))
        list_entries.append(entry)
        index_data = index_data[1:]  # delete null

    return list_entries


if __name__ == "__main__":
    pass
