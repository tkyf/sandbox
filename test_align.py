#!/usr/bin/env python
# coding:utf-8

import unittest
import align


class TestAlign(unittest.TestCase):

    def setUp(self):
        self.cases = [(("ABCDE", "ABDCE"), ""),
                        (("", "A"), ""),
                        (("A", ""), ""),
                        (("A", "D"), ""),
                        (("aa", "a"), ""),
                        (("a", "aa"), ""),
                        (("a", "a"), ""),
                        (("a", "ab"), ""),
                        (("ABCED", "ABDCE"), ""),
                        (("abcde", "abcde"), "")
                      ]

    def test_align(self):
        for case in self.cases:
            pass

if __name__ == '__main__':
    unittest.main()
