import os
from util.detect_dot_git import detect_dot_git


def read_head(path_in_repo: str) -> str:
    dot_git_dir = detect_dot_git(path_in_repo)
    head_path = os.path.join(dot_git_dir, "HEAD")
    with open(head_path, mode="r") as f:
        head_content = f.read().strip()
    return head_content


def get_head_hash(path_in_repo: str) -> str:
    dot_git_dir = detect_dot_git(path_in_repo)
    head_content = read_head(dot_git_dir)

    commit_hash: str
    if head_content.startswith("ref: "):
        refs_path = head_content.replace("ref: ", "").strip()
        refs_path = os.path.join(dot_git_dir, refs_path)
        with open(refs_path, mode="r") as f:
            commit_hash = f.read().strip()
    else:
        commit_hash = head_content.strip()
    return commit_hash


def get_current_branch(path_in_repo: str) -> str:
    dot_git_dir = detect_dot_git(path_in_repo)
    head_content = read_head(dot_git_dir)
    branch: str
    if head_content.startswith("ref: "):
        branch = head_content.replace("ref: refs/heads/", "")
    else:
        branch = ""
    return branch
