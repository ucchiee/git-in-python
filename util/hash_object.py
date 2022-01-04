from util.write_object import write_object


def hash_object(path: str) -> str:
    with open(path, mode="rb") as f:
        content: bytes = f.read()

    sha1_hash = write_object("blob", content, path)
    return sha1_hash
