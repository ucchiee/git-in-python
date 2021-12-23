import os
import shutil
import unittest

from commands import cmd_hash_object, cmd_init
from options import get_parser

dirname: str = os.path.abspath("./tmp_dir_hash")


class TestGipHashObject(unittest.TestCase):
    def setUp(self) -> None:
        # make git repo
        os.makedirs(dirname, exist_ok=True)
        parser = get_parser()
        args = parser.parse_args(["init", dirname])
        cmd_init(args)

        # add test file
        test_path = os.path.join(dirname, "README.md")
        with open(test_path, mode="w") as f:
            f.write("# test\n\nThis is a test file.")

    def tearDown(self) -> None:
        shutil.rmtree(dirname)

    def test_hash_object_text(self):
        os.chdir(dirname)
        parser = get_parser()
        args = parser.parse_args(["hash-object", "README.md"])
        self.assertNotEqual(args, None)
        sha1_hash = cmd_hash_object(args)
        self.assertEqual(sha1_hash, "1ac21c5f405ba481cf68620ac7802d3ac62adeef")


if __name__ == "__main__":
    unittest.main()
