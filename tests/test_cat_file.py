import os
import shutil
import subprocess
import unittest

from commands import cmd_cat_file
from options import get_parser

tests_dir = os.path.abspath(os.path.dirname(__file__))
dirname: str = os.path.join(tests_dir, "test_repo_cat")


class TestGipCatFile(unittest.TestCase):
    # def setUp(self) -> None:
    #     # make git repo
    #     os.makedirs(dirname, exist_ok=True)

    # def tearDown(self) -> None:
    #     dot_git_dir = os.path.join(dirname, ".git")
    #     shutil.rmtree(dot_git_dir)
    def get_hash(self, filename: str):
        # TODO: run git to get hash, should not use ??
        cmd = f"cd {dirname};git hash-object {filename}"
        proc = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE)
        return proc.stdout.strip()

    def get_result(self, hash_value: str):
        parser = get_parser()
        args = parser.parse_args(["cat-file", hash_value])
        return cmd_cat_file(args)

    def test_cat_file_text(self):
        os.chdir(dirname)

        filename: str = "test.c"
        hash_value = self.get_hash(filename)

        result = self.get_result(hash_value)
        self.assertIsNotNone(result)

        with open(filename, mode="r") as f:
            contents = f.read()
        self.assertEqual(result, contents)

    def test_cat_file_mutibyte_text(self):
        os.chdir(dirname)

        filename: str = "japanese.txt"
        hash_value = self.get_hash(filename)

        result = self.get_result(hash_value)
        self.assertIsNotNone(result)

        with open(filename, mode="r") as f:
            contents = f.read()
        self.assertEqual(result, contents)

    def test_cat_file_binary(self):
        os.chdir(dirname)

        filename: str = "a.out"
        hash_value = self.get_hash(filename)

        result = self.get_result(hash_value)
        self.assertIsNotNone(result)

        with open(filename, mode="r") as f:
            contents = f.read()
        self.assertEqual(result, contents)

    def test_cat_file_shorter_hash(self):
        os.chdir(dirname)

        filename: str = "test.c"
        hash_value = self.get_hash(filename)

        result = self.get_result(hash_value[:4])
        self.assertIsNotNone(result)

        with open(filename, mode="r") as f:
            contents = f.read()
        self.assertEqual(result, contents)

    def test_cat_file_too_short_hash(self):
        result = self.get_result("asd")
        print(f"result of adsfadsf: {result}")
        self.assertEqual(result, "")

    def test_cat_file_invalid_hash(self):
        result = self.get_result("asdfasdf")
        print(f"result of adsfadsf: {result}")
        self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()
