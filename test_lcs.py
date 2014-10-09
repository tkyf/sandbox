#!/usr/bin/env python
# coding:utf-8

import unittest
import lcs


class TestLCS(unittest.TestCase):

    def setUp(self):
        self.cases = [(("ABCDE", "ABDCE"), "ABDE"),
                        (("", "A"), ""),
                        (("A", ""), ""),
                        (("A", "D"), ""),
                        (("aa", "a"), "a"),
                        (("a", "aa"), "a"),
                        (("a", "a"), "a"),
                        (("a", "ab"), "a"),
                        (("ABCED", "ABDCE"), "ABCE")
                      ]

    def test_lcs(self):
        for case in self.cases:
            self.assertEqual(lcs.lcs(case[0][0], case[0][1]), case[1])

    def test_lcs_length(self):
        for case in self.cases:
            self.assertEqual(lcs.Table(case[0][1], case[0][1]).get_lcs_length(), len(case[1]))

    def test_recursive_lcs(self):
        for case in self.cases:
            self.assertEqual(lcs.recursive_lcs(case[0][0], case[0][1]), case[1])


if __name__ == '__main__':
    unittest.main()
