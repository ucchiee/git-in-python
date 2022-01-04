import struct
import os
from hashlib import sha1

from classes import IndexEntry
from util.detect_dot_git import detect_dot_git


def write_index(entries: list[IndexEntry]) -> None:
    entries.sort(key=lambda x: x.path)
    entry_data: bytes = b""

    # pack each entries
    for e in entries:
        index_entry: bytes = struct.pack(
            "!LLLLLLLLLL20sH",
            e.ctime_s,
            e.ctime_n,
            e.mtime_s,
            e.mtime_n,
            e.dev,
            e.ino,
            e.mode,
            e.uid,
            e.gid,
            e.size,
            e.sha1,
            e.flags,
        )
        path = e.path.encode()
        len_entry = ((62 + len(e.path) + 8) // 8) * 8  # null pading
        index_entry = index_entry + path + b"\x00" * (len_entry - 62 - len(path))
        entry_data += index_entry

    header = struct.pack("!4sLL", b"DIRC", 2, len(entries))
    index = header + entry_data
    index += sha1(index).digest()

    dot_git_dir = detect_dot_git(os.getcwd())
    index_path = os.path.join(dot_git_dir, "index")
    with open(index_path, mode="wb") as f:
        f.write(index)


if __name__ == "__main__":
    pass
