import os
from argparse import Namespace


def cmd_init(args: Namespace) -> None:
    dir = os.path.abspath(args.directory)
    dot_git_dir = os.path.join(dir, ".git")

    if os.path.exists(dot_git_dir):
        print("Reinitialized existing ", end="")
    else:
        print("Initialized empty ", end="")

    objects_dir = os.path.join(dot_git_dir, "objects")
    heads_dir = os.path.join(dot_git_dir, "heads")
    os.makedirs(objects_dir, exist_ok=True)
    os.makedirs(heads_dir, exist_ok=True)

    head_path = os.path.join(dot_git_dir, "HEAD")
    with open(head_path, mode="w") as f:
        f.write("ref: refs/heads/master\n")

    print(f"Gip repository in {dot_git_dir}")
