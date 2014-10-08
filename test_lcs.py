#!/usr/bin/env python
# conding:utf-8

import unittest
import lcs


class TestLCS(unittest.TestCase):

    def setup(self):
        pass

    def test_lcs(self):
        self.assertEqual(lcs.lcs("ABCDE", "ABDCE"), "ABDE")
        self.assertEqual(lcs.lcs("", "A"), "")
        self.assertEqual(lcs.lcs("A", ""), "")
        self.assertEqual(lcs.lcs("A", "D"), "")
        self.assertEqual(lcs.lcs("aa", "a"), "a")
        self.assertEqual(lcs.lcs("a", "aa"), "a")
        self.assertEqual(lcs.lcs("a", "a"), "a")

    def test_recursive_lcs(self):
        self.assertEqual(lcs.recursive_lcs("ABCDE", "ABDCE"), "ABDE")
        self.assertEqual(lcs.lcs("", "A"), "")
        self.assertEqual(lcs.lcs("A", ""), "")
        self.assertEqual(lcs.lcs("A", "D"), "")
        self.assertEqual(lcs.lcs("aa", "a"), "a")
        self.assertEqual(lcs.lcs("a", "aa"), "a")
        self.assertEqual(lcs.lcs("a", "a"), "a")

if __name__ == '__main__':
    unittest.main()
