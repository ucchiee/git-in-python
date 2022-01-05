import os

from util.objects import read_object, write_object
from util.read_index import read_index


def write_tree(path_in_repo: str) -> str:
    t_entry: bytes = b""
    for i_entry in read_index(path_in_repo):
        t_entry += f"{i_entry.mode:o} {i_entry.path}".encode()
        t_entry += b"\x00" + i_entry.sha1
    sha1_hash = write_object("tree", t_entry, os.getcwd())
    return sha1_hash


def parse_tree(contents: bytes) -> list[tuple[str, str, str]]:
    entries: list = []
    # parse tree
    while len(contents) > 20:
        nul_idx = contents.index(b"\x00")
        mode, path = contents[:nul_idx].decode().split(" ")
        contents = contents[nul_idx + 1 :]
        sha1_hash = contents[:20].hex()
        contents = contents[20:]

        entries.append((mode, path, sha1_hash))
    return entries


def read_tree(path_in_repo: str, hash_value: str) -> list[tuple[str, str, str]]:
    contents: bytes
    _type, contents = read_object(hash_value, path_in_repo)
    assert _type == "tree", f"{hash_value} is not a tree object"
    return parse_tree(contents)
