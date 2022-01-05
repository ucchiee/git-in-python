from util.objects import read_object


def parse_commit(hash_value: str, path_in_repo) -> dict:
    """
    only parse tree and parent
    """
    contents: bytes
    _type, contents = read_object(hash_value, path_in_repo)
    assert _type == "commit", "not a commit object"

    result: dict = dict()
    lines: list[str] = contents.decode().strip().split("\n")
    for line in lines:
        if line == "\n":
            continue

        line_list = line.split(" ")
        key = line_list[0]
        if key == "tree":
            result[key] = line_list[1]
        elif key == "parent":
            if key not in result:
                result[key] = []
            result[key].append(line_list[1])
        else:
            break
    return result
