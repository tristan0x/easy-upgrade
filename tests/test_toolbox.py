import os
import os.path as osp
import tempfile
import unittest

from easy_upgrade.toolbox import (
    find_executable,
    pushd,
    temp_dir,
)


class ToolboxTest(unittest.TestCase):
    def test_pushd(self):
        temp_dir = tempfile.mkdtemp()
        orig_dir = os.getcwd()
        with pushd(temp_dir) as d:
            self.assertEqual(d, temp_dir)
            self.assertTrue(os.getcwd(), temp_dir)
        self.assertTrue(os.getcwd(), orig_dir)

    def test_find_executable(self):
        self.assertEqual(find_executable(__file__), __file__)
        with self.assertRaises(Exception):
            find_executable("unknown-command-foo")
        with self.assertRaises(Exception):
            find_executable("unknown-command-foo", 'unknown-command-foo2')
        self.assertIsNone(find_executable(
            "unknown-command-foo",
            raise_if_missing=False
        ))

    def test_temp_dir(self):
        with temp_dir() as d:
            self.assertTrue(osp.isdir(d))
        self.assertFalse(osp.isdir(d))
        with temp_dir(cleanup=False) as d:
            self.assertTrue(osp.isdir(d))
        self.assertTrue(osp.isdir(d))
