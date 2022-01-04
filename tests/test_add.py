import os
import shutil
import unittest

from commands import cmd_add, cmd_hash_object, cmd_init
from options import get_parser
from util import read_index, get_path_in_repo

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

    def check_index(self, filename: str) -> None:
        parser = get_parser()
        args = parser.parse_args(["hash-object", filename])
        sha1_hash = cmd_hash_object(args)
        args = parser.parse_args(["add", filename])
        cmd_add(args)

        statinfo = os.stat(filename)
        filename = get_path_in_repo(filename)
        entries = read_index(os.getcwd())
        # self.assertEqual(len(entries), 1)  # need to inspect
        e = entries[0]
        self.assertEqual(int(statinfo.st_ctime), e.ctime_s)
        self.assertEqual(int(statinfo.st_ctime_ns) & 0xFFFFFFFF, e.ctime_n)
        self.assertEqual(int(statinfo.st_mtime), e.mtime_s)
        self.assertEqual(int(statinfo.st_mtime_ns) & 0xFFFFFFFF, e.mtime_n)
        self.assertEqual(statinfo.st_dev, e.dev)
        self.assertEqual(statinfo.st_ino, e.ino)
        self.assertEqual(statinfo.st_mode, e.mode)
        self.assertEqual(statinfo.st_uid, e.uid)
        self.assertEqual(statinfo.st_gid, e.gid)
        self.assertEqual(statinfo.st_size, e.size)
        self.assertEqual(sha1_hash, e.sha1.hex())
        len_path = len(filename)
        self.assertEqual(len_path, e.flags)
        self.assertEqual(filename, e.path)

    def test_add_text(self):
        os.chdir(dirname)
        self.check_index("test.c")

    def test_add_text_multibyte(self):
        os.chdir(dirname)
        self.check_index("japanese.txt")

    def test_add_text_binary(self):
        os.chdir(dirname)
        self.check_index("a.out")

    def test_add_file_in_dir(self):
        os.chdir(os.path.join(dirname, "dir"))
        self.check_index("test.py")


if __name__ == "__main__":
    unittest.main()
