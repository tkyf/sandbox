#!/usr/bin/env python
# conding:utf-8

import unittest
import lcs


class TestLCS(unittest.TestCase):

    def setup(self):
        pass

    def test_lcs(self):
        self.assertEqual(lcs.lcs("ABCDE", "ABDCE"), "ABCE")

if __name__ == '__main__':
    unittest.main()
