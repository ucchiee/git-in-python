import glob
import os
import zlib
from hashlib import sha1

from util.detect_dot_git import detect_dot_git


def write_object(_type: str, data: bytes, path_in_repo: str) -> str:
    valid_obj = set(["blob", "tree", "commit"])
    assert _type in valid_obj, "invalid object type"

    header: str = f"{_type} {len(data)}\0"
    contents: bytes = header.encode() + data
    sha1_hash: str = sha1(contents).hexdigest()
    contents = zlib.compress(contents)

    # calc path
    dot_git_dir = detect_dot_git(path_in_repo)
    dirname, filename = sha1_hash[:2], sha1_hash[2:]
    obj_dir: str = os.path.join(dot_git_dir, "objects", dirname)
    os.makedirs(obj_dir, exist_ok=True)
    obj_path: str = os.path.join(obj_dir, filename)

    with open(obj_path, mode="wb") as f:  # type: ignore
        f.write(contents)  # type: ignore

    return sha1_hash


def read_object(hash_value: str, path_in_repo: str) -> tuple[str, bytes]:
    dot_git_dir: str = detect_dot_git(path_in_repo)
    obj_dir: str = os.path.join(dot_git_dir, "objects")

    # object is stored in f".git/objects/{hash_value[:2]}/{hash_value[2:]}"
    # hash_value doesn't need to be complete as long as we can specify unique obj
    obj_path = os.path.join(obj_dir, hash_value[:2], f"{hash_value[2:]}*")
    obj_path_list = glob.glob(obj_path)
    if len(obj_path_list) != 1:
        raise ValueError

    with open(obj_path_list[0], mode="rb") as f:
        contents = f.read()
    contents = zlib.decompress(contents)

    spc_idx = contents.index(b"\x20")
    _type = contents[:spc_idx].decode()
    # contents = contents[5:]
    nul_idx = contents.index("\0".encode())
    # print(f"header : {contents[:nul_idx].decode()}")
    return _type, contents[nul_idx + 1 :]
