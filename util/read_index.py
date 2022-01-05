import os
import struct
from hashlib import sha1

from classes import IndexEntry
from util.detect_dot_git import detect_dot_git


def read_index(path_in_repo: str, print_error: bool = False) -> list[IndexEntry]:
    dot_git_dir: str = detect_dot_git(path_in_repo)
    assert dot_git_dir, "Not in a git repository"

    index_path: str = os.path.join(dot_git_dir, "index")
    if not os.path.exists(index_path):
        return []

    with open(index_path, mode="rb") as f:
        index_data: bytes = f.read()

    checksum: bytes = sha1(index_data[:-20]).digest()
    assert checksum == index_data[-20:], "invalid index"

    signature, version, num_entries = struct.unpack("!4sLL", index_data[:12])
    assert signature == b"DIRC", "invalid signature, must be DIRC"
    if version != 2:
        if print_error:
            print(f"do not support {version}, only support 2")
        return []

    index_data = index_data[12:-20]
    list_entries = []
    i = 0
    while i + 62 < len(index_data):
        # parse first 62 bytes
        fields_end = i + 62
        fields = struct.unpack("!LLLLLLLLLL20sH", index_data[i:fields_end])

        # parse path
        path_end = index_data.index(b"\x00", fields_end)
        path = index_data[fields_end:path_end]

        entry = IndexEntry(*(fields + (path.decode(),)))
        list_entries.append(entry)
        entry_len = ((62 + len(path) + 8) // 8) * 8
        i += entry_len

    assert len(list_entries) == num_entries
    return list_entries


if __name__ == "__main__":
    pass
