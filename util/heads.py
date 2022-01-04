import os
from util.detect_dot_git import detect_dot_git


def _read_head(path_in_repo: str) -> str:
    dot_git_dir = detect_dot_git(path_in_repo)
    head_path = os.path.join(dot_git_dir, "HEAD")
    if not os.path.exists(head_path):
        return ""
    with open(head_path, mode="r") as f:
        head_content = f.read().strip()
    return head_content


def _write_head(path_in_repo: str, contents: str) -> None:
    dot_git_dir = detect_dot_git(path_in_repo)
    head_path = os.path.join(dot_git_dir, "HEAD")
    with open(head_path, mode="w") as f:
        f.write(contents)


def _read_branch(path_in_repo: str, branch: str) -> str:
    dot_git_dir = detect_dot_git(path_in_repo)
    ref_path = os.path.join(dot_git_dir, "refs", "heads", branch)
    if not os.path.exists(ref_path):
        return ""
    with open(ref_path, mode="r") as f:
        branch_content = f.read().strip()
    return branch_content


def _write_branch(path_in_repo: str, branch: str, contents: str) -> None:
    dot_git_dir = detect_dot_git(path_in_repo)
    ref_path = os.path.join(dot_git_dir, "refs", "heads", branch)
    with open(ref_path, mode="w") as f:
        f.write(contents)


def get_current_branch(path_in_repo: str) -> str:
    dot_git_dir = detect_dot_git(path_in_repo)
    head_content = _read_head(dot_git_dir)
    branch: str
    if head_content.startswith("ref: "):
        branch = head_content.replace("ref: refs/heads/", "")
    else:
        branch = ""
    return branch


def read_head_hash(path_in_repo: str) -> str:
    dot_git_dir = detect_dot_git(path_in_repo)
    branch = get_current_branch(path_in_repo)
    if branch:
        return _read_branch(dot_git_dir, branch)
    else:
        return _read_head(dot_git_dir)


def write_head_hash(path_in_repo: str, hash: str) -> None:
    dot_git_dir = detect_dot_git(path_in_repo)
    branch = get_current_branch(dot_git_dir)
    if branch:
        _write_branch(dot_git_dir, branch, hash)
    else:
        _write_head(dot_git_dir, hash)
