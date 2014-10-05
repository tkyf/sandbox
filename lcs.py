#!/usr/bin/env python
# coding:utf-8

from __future__ import print_function
import sys


def lcs(str1, str2):
    """Calculate Longest Common subsequence of two strings.

    param: str1: one of strings.
    param: str2: the other one of strings.
    """
    table = Table(str1, str2)
    print(table)


class Cell(object):
    def __init__(self):
        self.score = 0

    def __str__(self):
        return self.score


class Table(object):
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

        self.table = []
        self.initialize()

    def __str__(self):
        return str(self.table)

    def initialize(self):
        self.initialize_table()
        self.initialize_pointers()

    def initialize_table(self):
        self.table = [[Cell() for j in range(len(self.str1))] for i in range(len(self.str2))]

    def initialize_pointers(self):
        pass

    def fill_in(self):
        pass

    def trace_back(self):
        pass


def recursive_lcs(str1, str2):
    if str1 == '' or str2 == '':
        return ''
    else:
        c1, str1_dash = str1[-1], str1[:-1]
        c2, str2_dash = str2[-1], str2[:-1]
        L1 = recursive_lcs(str1_dash, str2)
        L2 = recursive_lcs(str1, str2_dash)
        L3 = recursive_lcs(str1_dash, str2_dash)
        if c1 == c2:
            return longest_string(L1, L2, L3 + c1)
        else:
            return longest_string(L1, L2, L3)


def longest_string(*strings):
    return sorted(strings, key=len)[-1]


def main():
    if len(sys.argv) != 3:
        print('Usage: $ python LCS.py string1 string2')
        return 1

    # print(recursive_lcs(sys.argv[1], sys.argv[2]))
    lcs(sys.argv[1], sys.argv[2])
    return 0


if __name__ == '__main__':
    sys.exit(main())
