import os
import shutil
import unittest

from commands import cmd_init
from options import get_parser

tests_dir = os.path.abspath(os.path.dirname(__file__))
dirname: str = os.path.join(tests_dir, "test_repo")


class TestGipCatFile(unittest.TestCase):
    def setUp(self) -> None:
        # make git repo
        os.makedirs(dirname, exist_ok=True)
        parser = get_parser()
        args = parser.parse_args(["init", dirname])
        cmd_init(args)

    def tearDown(self) -> None:
        dot_git_dir = os.path.join(dirname, ".git")
        shutil.rmtree(dot_git_dir)

    def test_cat_file_text(self):
        os.chdir(dirname)

    def test_cat_file_mutibyte_text(self):
        os.chdir(dirname)

    def test_cat_file_binary(self):
        os.chdir(dirname)


if __name__ == "__main__":
    unittest.main()
