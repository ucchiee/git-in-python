import os
import time
from argparse import Namespace

from util import get_current_branch, read_branch, write_branch, write_object, write_tree


def cmd_commit(args: Namespace) -> str:
    branch = get_current_branch(os.getcwd())
    parent_hash = read_branch(os.getcwd(), branch)
    if not branch:
        print(f"now at commit {parent_hash}, please checkout to a branch")
        return ""
    tree_hash = write_tree(os.getcwd())
    timestamp = str(int(time.mktime(time.localtime())))
    utc_offset = -time.timezone
    timestamp += " +" if utc_offset > 0 else " -"
    timestamp += f"{utc_offset // 3600:02}"
    timestamp += f"{(utc_offset % 3600) // 60:02}"

    contents: bytes
    contents = f"tree {tree_hash}\n".encode()
    if parent_hash:
        contents += f"parent {parent_hash}\n".encode()
    contents += f"author {args.author} <{args.email}>{timestamp}\n".encode()
    contents += f"committer {args.author} <{args.email}>{timestamp}\n".encode()
    contents += "\n".encode()
    contents += f"{args.message}\n".encode()
    commit_hash = write_object("commit", contents, os.getcwd())
    write_branch(os.getcwd(), branch, commit_hash)
    print(f"committed to {branch} {commit_hash}")
    return commit_hash
