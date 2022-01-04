from util.objects import read_object


def cat_blob(contents: bytes) -> str:
    return contents.decode(errors="replace")


def cat_tree(contents: bytes, path_in_repo: str) -> str:

    # parse each entry
    result: str = ""
    while len(contents) > 20:
        nul_idx = contents.index(b"\x00")
        mode, path = contents[:nul_idx].decode().split(" ")
        contents = contents[nul_idx + 1 :]
        sha1_hash = contents[:20].hex()
        contents = contents[20:]

        # detect obj type
        try:
            _type, _ = read_object(sha1_hash, path_in_repo)
        except ValueError:
            print(f"{sha1_hash}")
            _type = ""

        result = f"{mode} {_type} {sha1_hash}  {path}\n"
    return result


def cat_commit(contents: bytes) -> str:
    return contents.decode(errors="replace")


def cat_file(hash_value: str, path_in_repo: str) -> str:
    try:
        obj_type, contents = read_object(hash_value, path_in_repo)
    except ValueError:
        return ""

    if obj_type == "blob":
        result = cat_blob(contents)
    elif obj_type == "tree":
        result = cat_tree(contents, path_in_repo)
    elif obj_type == "commit":
        result = cat_commit(contents)
    else:
        assert False, "Invalid or not supported object type"
    return result


if __name__ == "__main__":
    pass
