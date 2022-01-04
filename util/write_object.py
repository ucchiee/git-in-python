import os
import zlib
from hashlib import sha1

from util.detect_dot_git import detect_dot_git


def write_object(_type: str, data: bytes, path_in_repo) -> str:
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
