import unittest

from commands import cmd_hash_object
from options import get_parser


class TestGipHashObject(unittest.TestCase):
    def test_hash_object(self):
        parser = get_parser()
        args = parser.parse_args(["hash-object", "README.md"])
        cmd_hash_object(args)


if __name__ == "__main__":
    unittest.main()
