import os
import shutil
import unittest
import subprocess

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

    def test_hash_object_text(self):
        os.chdir(dirname)
        parser = get_parser()
        args = parser.parse_args(["hash-object", "test.c"])
        sha1_hash = cmd_hash_object(args)
        proc = subprocess.run("git hash-object test.c", shell=True, text=True, stdout=subprocess.PIPE)
        self.assertEqual(sha1_hash, proc.stdout.strip())

    def test_hash_object_multibytes_text(self):
        os.chdir(dirname)
        parser = get_parser()
        args = parser.parse_args(["hash-object", "japanese.txt"])
        sha1_hash = cmd_hash_object(args)
        proc = subprocess.run("git hash-object japanese.txt", shell=True, text=True, stdout=subprocess.PIPE)
        self.assertEqual(sha1_hash, proc.stdout.strip())

    def test_hash_object_binary(self):
        os.chdir(dirname)
        parser = get_parser()
        args = parser.parse_args(["hash-object", "a.out"])
        sha1_hash = cmd_hash_object(args)
        proc = subprocess.run("git hash-object a.out", shell=True, text=True, stdout=subprocess.PIPE)
        self.assertEqual(sha1_hash, proc.stdout.strip())


if __name__ == "__main__":
    unittest.main()
