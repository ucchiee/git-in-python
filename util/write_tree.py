import os

from util.read_index import read_index
from util.objects import write_object


def write_tree(path_in_repo) -> str:
    t_entry: bytes = b""
    for i_entry in read_index(path_in_repo):
        t_entry += f"{i_entry.mode:o} {i_entry.path}".encode()
        t_entry += b"\x00" + i_entry.sha1
    sha1_hash = write_object("tree", t_entry, os.getcwd())
    return sha1_hash
