import os
import shutil
import unittest

from commands import cmd_add, cmd_commit, cmd_hash_object, cmd_init, cmd_write_tree
from options import get_parser
from util import parse_commit

tests_dir = os.path.abspath(os.path.dirname(__file__))
dirname: str = os.path.join(tests_dir, "test_repo")


class TestGipCommit(unittest.TestCase):
    def setUp(self) -> None:
        # make git repo
        os.makedirs(dirname, exist_ok=True)
        parser = get_parser()
        args = parser.parse_args(["init", dirname])
        cmd_init(args)

    def tearDown(self) -> None:
        dot_git_dir = os.path.join(dirname, ".git")
        shutil.rmtree(dot_git_dir)

    def check_commit(self, filename: str, parent_hash: list[str] = []) -> str:
        parser = get_parser()
        args = parser.parse_args(["hash-object", filename])
        cmd_hash_object(args)
        args = parser.parse_args(["add", filename])
        cmd_add(args)
        args = parser.parse_args(["write-tree"])
        tree_hash = cmd_write_tree(args)

        # commit
        args = parser.parse_args(["commit"])
        commit_hash = cmd_commit(args)
        commit_dict = parse_commit(commit_hash, dirname)
        self.assertEqual(tree_hash, commit_dict["tree"])
        if parent_hash:
            self.assertEqual(parent_hash, commit_dict["parent"])

        return commit_hash

    def test_commit_text(self):
        os.chdir(dirname)
        self.check_commit("test.c")

    def test_commit_multibyte(self):
        os.chdir(dirname)
        self.check_commit("japanese.txt")

    def test_commit_binary(self):
        os.chdir(dirname)
        self.check_commit("a.out")


if __name__ == "__main__":
    unittest.main()
