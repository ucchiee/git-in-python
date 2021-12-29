import os
import glob
import zlib

from util.detect_dot_git import detect_dot_git


def cat_file(hash_value: str, print_error: bool = False) -> str:
    # can't specify obj
    if len(hash_value) < 4:
        if print_error:
            print(f"fatal: Not a valid object name {hash_value}")
        return ""

    dot_git_dir: str = detect_dot_git(os.getcwd())
    obj_dir: str = os.path.join(dot_git_dir, "objects")

    # object is stored in f".git/objects/{hash_value[:2]}/{hash_value[2:]}"
    # hash_value doesn't need to be complete as long as we can specify unique obj
    obj_path = os.path.join(obj_dir, hash_value[:2], f"{hash_value[2:]}*")
    obj_path_list = glob.glob(obj_path)
    if len(obj_path_list) == 0:
        if print_error:
            print(f"there is no object that starts with {hash_value}")
        return ""
    elif len(obj_path_list) > 1:
        if print_error:
            print(f"can't specify unique object by {hash_value}")
        return ""

    with open(obj_path_list[0], mode="rb") as f:
        contents = f.read()
    contents = zlib.decompress(contents)

    # remove prefix of blob
    # TODO: need check other object type
    for i, byte in enumerate(contents):
        if byte == 0:
            break
    contents = contents[i + 1 :]

    result = contents.decode(errors="replace")
    return result


if __name__ == "__main__":
    pass
