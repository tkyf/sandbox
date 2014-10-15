#!/usr/bin/env python
# coding:utf-8

from __future__ import print_function
import sys


def lcs(str1, str2):
    """Calculate Longest Common Subsequence of two strings.

    param: str1: one of strings.
    param: str2: the other one of strings.
    """
    if str1 == "" or str2 == "":
        return ""

    table = Table(str1, str2)
    return table.get_lcs()


class Table(object):
    """Table for calcuration LCS by dynamic programming.
    """

    class Cell(object):
        """One of cell in tabel.
        """
        def __init__(self, table, row, col):
            self.table = table
            self.row = row
            self.col = col
            self.score = 0
            self.prev_cell = None

        def __str__(self):
            return str(self.score)

        def fill_in_cell(self, above_cell, left_cell, aboveleft_cell):
            V1 = left_cell.score
            V2 = above_cell.score
            if self.table.str1[self.col - 1] == self.table.str2[self.row - 1]:
                V3 = aboveleft_cell.score + 1
            else:
                V3 = aboveleft_cell.score

            score = max(V1, V2, V3)

            if score == V3:
                self.prev_cell = aboveleft_cell
            elif score == V2:
                self.prev_cell = above_cell
            else:
                self.prev_cell = left_cell

            self.score = score

    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

        self.table = []
        self._initialize()

    def __str__(self):
        return str([[str(cell) for cell in row] for row in self.table])

    def _initialize(self):
        self.table = [[Table.Cell(self, i, j) for j in range(len(self.str1) + 1)] for i in range(len(self.str2) + 1)]

    # Calcurate LCS
    def get_lcs(self):
        if not hasattr(self, 'lcs'):
            self._fill_in()
            self.lcs = self._get_trace_back()
        return self.lcs

    def get_lcs_length(self):
        if not hasattr(self, 'lcs'):
            self.get_lcs()

        return self.table[-1][-1].score

    def _fill_in(self):
        for i, row in enumerate(self.table):
            if i == 0:
                continue
            for j, cell in enumerate(row):
                if j == 0:
                    continue

                above     = self.table[i - 1][j]
                left      = self.table[i][j - 1]
                aboveleft = self.table[i - 1][j - 1]
                cell.fill_in_cell(above, left, aboveleft)

    def _get_trace_back(self):
        lcs = ""
        current_cell = self.table[len(self.str2)][len(self.str1)]
        while current_cell.score > 0:
            prev_cell = current_cell.prev_cell
            if current_cell.score - prev_cell.score == 1 \
               and current_cell.row - prev_cell.row == 1 \
               and current_cell.col - prev_cell.col == 1:
                lcs = self.str1[current_cell.col - 1] + lcs
            current_cell = prev_cell
        return lcs

    def print_table(self):
        if not hasattr(self, 'lcs'):
            self.get_lcs()
        print("          " + "    ".join(self.str1))
        print("   " + str([str(cell) for cell in self.table[0]]))
        for i, c in enumerate(self.str2):
            if i == 0:
                continue
            print(" {0} {1}".format(c, [str(cell) for cell in self.table[i]]))


def recursive_lcs(str1, str2):
    if str1 == '' or str2 == '':
        return ''
    else:
        c1, str1_rest = str1[-1], str1[:-1]
        c2, str2_rest = str2[-1], str2[:-1]
        L1 = recursive_lcs(str1_rest, str2)
        L2 = recursive_lcs(str1, str2_rest)
        L3 = recursive_lcs(str1_rest, str2_rest)
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

    lcs(sys.argv[1], sys.argv[2])

    return 0


if __name__ == '__main__':
    sys.exit(main())
