import zlib
import os
from hashlib import sha1

from util.detect_dot_git import detect_dot_git


def hash_object(path: str) -> str:
    dot_git_dir = detect_dot_git(path)

    with open(path, mode="rb") as f:
        content: bytes = f.read()
    header: str = f"blob {len(content)}\0"
    store: bytes = header.encode() + content
    content_zlib = zlib.compress(store)
    sha1_hash: str = sha1(store).hexdigest()

    # write object
    dirname, filename = sha1_hash[:2], sha1_hash[2:]
    obj_dir: str = os.path.join(dot_git_dir, "objects", dirname)
    os.makedirs(obj_dir, exist_ok=True)
    obj_path: str = os.path.join(obj_dir, filename)
    with open(obj_path, mode="wb") as f:  # type: ignore
        f.write(content_zlib)  # type: ignore

    return sha1_hash
