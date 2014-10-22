#!/usr/bin/env python
# coding:utf-8

from __future__ import print_function
import sys


def align(str1, str2):
    """Calculate global alignment of two strings with Needleman-Wunsch algorithm.

    param: str1: one of strings.
    param: str2: the other one of strings.
    """
    if str1 == "" or str2 == "":
        return ""

    table = Table(str1, str2)
    table.print_table()

    return ""


class Table(object):
    """Table for calcuration global alignment by dynamic programming.
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

        def initialize_score(self):
            if self.row == 0 and self.col != 0:
                print(self.row, self.col)
                self.score = self.table.score_table[self.row][self.col - 1].score - 2
                print(self.score)
            elif self.row != 0 and self.col == 0:
                print(self.row, self.col)
                self.score = self.table.score_table[self.row - 1][self.col].score - 2
                print(self.score)
            else:
                self.score = 0

        def initialize_prev_cell(self):
            if self.row == 0 and self.col != 0:
                self.prev_cell = self.table.score_table[self.row][self.col - 1]
            elif self.row != 0 and self.col == 0:
                self.prev_cell = self.table.score_table[self.row - 1][self.col]
            else:
                self.prev_cell = None

        def __str__(self):
            return str(self.score)

        def fill_in_cell(self, above_cell, left_cell, aboveleft_cell):
            from_left_score = left_cell.score - 2
            from_above_score = above_cell.score - 2
            if (self.table.str1[self.row] == self.table.str2[self.col]):
                from_aboveleft_score = aboveleft_cell.score + 1
            else:
                from_aboveleft_score = aboveleft_cell.score - 1

            self.score = max(from_left_score, from_above_score, from_aboveleft_score)
            if (self.score == from_left_score):
                self.prev_cell = left_cell
            elif (self.score == from_above_score):
                self.prev_cell = above_cell
            else:
                self.prev_cell = aboveleft_cell

    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

        self.score_table = []
        self._initialize()

    def __str__(self):
        return str([[str(cell) for cell in row] for row in self.score_table])

    def _initialize(self):
        self.score_table = [[Table.Cell(self, i, j) for j in range(len(self.str1) + 1)] for i in range(len(self.str2) + 1)]
        for row in self.score_table:
            for cell in row:
                cell.initialize_score()
                cell.initialize_prev_cell()

    # Calcurate Global alignment
    def calcurate(self):
        if not hasattr(self, 'alignment'):
            self._fill_in()
            self.alignment = self._get_trace_back()

    def get_alignment(self):
        self.calcurate()
        return self.alignment

    def _fill_in(self):
        for i, row in enumerate(self.score_table):
            for j, cell in enumerate(row):
                above_cell = self.score_table[i - 1][j]
                left_cell = self.score_table[i][j - 1]
                leftabove_cell = self.score_table[i - 1][j - 1]
                cell.fill_in_cell(above_cell, left_cell, leftabove_cell)

    def _get_trace_back(self):
# TODO implement
        pass

    def print_table(self):
        self.calcurate()
        print("          " + "    ".join(self.str1))
        print("   " + str([str(cell) for cell in self.score_table[0]]))
        for i, c in enumerate(self.str2):
            if i == 0:
                continue
            print(" {0} {1}".format(c, [str(cell) for cell in self.score_table[i]]))


def main():
    if len(sys.argv) != 3:
        print('Usage: $ python align.py string1 string2')
        return 1

    align(sys.argv[1], sys.argv[2])

    return 0


if __name__ == '__main__':
    sys.exit(main())
