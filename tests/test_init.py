import unittest

from commands import cmd_init
from options import get_parser


class TestGipInit(unittest.TestCase):
    def test_with_dir(self):
        parser = get_parser()
        args = parser.parse_args(["init", "test_dir"])
        cmd_init(args)

    def test_without_dir(self):
        parser = get_parser()
        args = parser.parse_args(["init"])
        cmd_init(args)


if __name__ == "__main__":
    unittest.main()
