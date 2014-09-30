#!/usr/bin/env python
# coding:utf-8

from __future__ import print_function
import sys


def lcs(str1, str2):
    pass


def fill_in():
    pass


def trace_back():
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

    print(recursive_lcs(sys.argv[1], sys.argv[2]))
    return 0


if __name__ == '__main__':
    sys.exit(main())
