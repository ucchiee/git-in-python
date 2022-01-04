import os
from argparse import Namespace

from classes import IndexEntry
from util import hash_object, read_index, write_index


def cmd_add(args: Namespace) -> None:
    assert len(args.files) > 0
    index_entries: list[IndexEntry] = read_index(args.files[0])

    # delete entries for updated files
    index_entries = [e for e in index_entries if e.path not in args.files]

    args.files = [os.path.abspath(path) for path in args.files]

    # hash each file and add to index
    for path in args.files:
        statinfo = os.stat(path)
        sha1_bytes = bytes.fromhex(hash_object(path))
        len_path = len(path.encode())
        if len_path > 0xFFF:
            len_path = 0xFFF
        entry = IndexEntry(
            int(statinfo.st_ctime),
            statinfo.st_ctime_ns,
            int(statinfo.st_mtime),
            statinfo.st_mtime_ns,
            statinfo.st_dev,
            statinfo.st_ino,
            statinfo.st_mode,  # actually this value is wrong, git change file mode when added
            statinfo.st_uid,
            statinfo.st_gid,
            statinfo.st_size,
            sha1_bytes,
            len_path,
            path,
        )
        index_entries.append(entry)
    write_index(index_entries)


if __name__ == "__main__":
    pass
