#!/usr/bin/env python
# coding:utf-8

import unittest
import align


class TestAlign(unittest.TestCase):

    def setUp(self):
        self.cases = [(("A", "A"), ("A", "A")),
                      (("A", "B"), ("A", "B")),
                      (("AB", "A"), ("AB", "A-")),
                      (("BA", "A"), ("BA", "-A")),
                      (("ABA", "AA"), ("ABA", "A-A")),
                      (("BAB", "A"), ("BAB", "-A-")),
                      (("A", ""), ("A", "")),
                      (("", "A"), ("", "A")),
                      (("", ""), ("", ""))
                      ]

    def test_align(self):
        for case in self.cases:
            self.assertEqual(align.align(case[0][0], case[0][1]), case[1])

if __name__ == '__main__':
    unittest.main()
