import os
from argparse import Namespace

from classes import IndexEntry
from util import hash_object, read_index, write_index, get_path_in_repo


def cmd_add(args: Namespace) -> None:
    assert len(args.files) > 0

    paths_in_repo = [get_path_in_repo(path) for path in args.files]

    index_entries: list[IndexEntry] = read_index(args.files[0])
    index_entries = [e for e in index_entries if e.path not in args.files]

    # hash each file and add to index
    for filename, path_to_add in zip(args.files, paths_in_repo):
        statinfo = os.stat(filename)
        sha1_bytes = bytes.fromhex(hash_object(filename))
        len_path = len(path_to_add.encode())
        if len_path > 0xFFF:
            len_path = 0xFFF
        entry = IndexEntry(
            int(statinfo.st_ctime),
            int(statinfo.st_ctime_ns) & 0xFFFFFFFF,  # can be 0
            int(statinfo.st_mtime),
            int(statinfo.st_mtime_ns) & 0xFFFFFFFF,  # can be 0
            statinfo.st_dev,
            statinfo.st_ino,
            statinfo.st_mode,  # actually this value is wrong, git change file mode when added
            statinfo.st_uid,
            statinfo.st_gid,
            statinfo.st_size,
            sha1_bytes,
            len_path,
            path_to_add,
        )
        index_entries.append(entry)
    write_index(index_entries)


if __name__ == "__main__":
    pass
