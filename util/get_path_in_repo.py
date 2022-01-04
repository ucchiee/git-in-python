import os

from util.detect_dot_git import detect_dot_git


def get_path_in_repo(path: str) -> str:
    dot_git_dir = detect_dot_git(path)
    repo_root = os.path.dirname(dot_git_dir)
    path = os.path.abspath(path)
    return path.replace(repo_root, "")[1:]
