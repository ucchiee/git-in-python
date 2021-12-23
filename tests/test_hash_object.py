import unittest
import os
import shutil

# from commands import cmd_hash_object
from options import get_parser

dirname: str = os.path.abspath("./tmp_dir")


class TestGipHashObject(unittest.TestCase):
    def setUp(self) -> None:
        os.makedirs(dirname, exist_ok=True)

    def tearDown(self) -> None:
        shutil.rmtree(dirname)

    def test_hash_object(self):
        parser = get_parser()
        args = parser.parse_args(["hash-object", "README.md"])
        self.assertNotEqual(args, None)
        # cmd_hash_object(args)


if __name__ == "__main__":
    unittest.main()
