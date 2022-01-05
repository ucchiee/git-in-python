import unittest
import os
import shutil

from commands import cmd_init
from options import get_parser

dirname: str = os.path.abspath("./tmp_dir")


class TestGipInit(unittest.TestCase):
    def setUp(self) -> None:
        os.makedirs(dirname, exist_ok=True)

    def tearDown(self) -> None:
        shutil.rmtree(dirname)

    def util_test_git_dir(self, dot_git_dir: str) -> None:
        objects_dir: str = os.path.join(dot_git_dir, "objects")
        heads_dir: str = os.path.join(dot_git_dir, "refs", "heads")
        head_path: str = os.path.join(dot_git_dir, "HEAD")
        self.assertTrue(os.path.exists(dot_git_dir))
        self.assertTrue(os.path.exists(objects_dir))
        self.assertTrue(os.path.exists(heads_dir))
        self.assertTrue(os.path.exists(head_path))

        with open(head_path, mode="r") as f:
            contents = f.read()
        self.assertEqual(contents, "ref: refs/heads/master\n")

    def test_with_dir(self):
        os.chdir(dirname)
        parser = get_parser()
        test_dir = os.path.join(dirname, "test_dir")
        args = parser.parse_args(["init", test_dir])
        cmd_init(args)

        dot_git_dir: str = os.path.join(test_dir, ".git")
        self.util_test_git_dir(dot_git_dir)

    def test_without_dir(self):
        os.chdir(dirname)
        parser = get_parser()
        args = parser.parse_args(["init"])
        cmd_init(args)

        dot_git_dir: str = os.path.join(dirname, ".git")
        self.util_test_git_dir(dot_git_dir)


if __name__ == "__main__":
    unittest.main()
