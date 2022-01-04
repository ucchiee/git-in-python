import os


def detect_dot_git(path: str) -> str:
    # check path
    if not os.path.exists(path):
        print(f"invalid path : {path}")
        return ""
    if path.endswith(".git"):
        return path

    # traverse to parent dir
    path = os.path.abspath(path)
    counter = 0
    while True:
        git_dir = os.path.join(path, ".git")
        if os.path.exists(git_dir):
            return git_dir

        if counter > 0:
            break
        if path == "/":
            counter += 1
        path = os.path.dirname(path)
    return ""


if __name__ == "__main__":
    git_dir = detect_dot_git("./")
    print(f"detected git dir : {git_dir}")
