import os
import shutil
import subprocess
import unittest

from commands import cmd_hash_object, cmd_init
from options import get_parser

tests_dir = os.path.abspath(os.path.dirname(__file__))
dirname: str = os.path.join(tests_dir, "test_repo")


class TestGipHashObject(unittest.TestCase):
    def setUp(self) -> None:
        # make git repo
        os.makedirs(dirname, exist_ok=True)
        parser = get_parser()
        args = parser.parse_args(["init", dirname])
        cmd_init(args)

    def tearDown(self) -> None:
        dot_git_dir = os.path.join(dirname, ".git")
        shutil.rmtree(dot_git_dir)

    def check_hash(self, filename: str) -> None:
        parser = get_parser()
        args = parser.parse_args(["hash-object", filename])
        sha1_hash = cmd_hash_object(args)
        proc = subprocess.run(f"git hash-object {filename}", shell=True, text=True, stdout=subprocess.PIPE)
        self.assertEqual(sha1_hash, proc.stdout.strip())

    def test_hash_object_text(self):
        os.chdir(dirname)
        self.check_hash("test.c")

    def test_hash_object_multibytes_text(self):
        os.chdir(dirname)
        self.check_hash("japanese.txt")

    def test_hash_object_binary(self):
        os.chdir(dirname)
        self.check_hash("a.out")

    def test_hash_object_in_dir(self):
        os.chdir(os.path.join(dirname, "dir"))
        self.check_hash("test.py")


if __name__ == "__main__":
    unittest.main()
