#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#
def bomberMan(n, grid):
    if n == 1:
        return grid

    if n % 2 == 0:
        return ['O' * len(grid[0]) for _ in grid]

    def explode(g):
        R = len(g)
        C = len(g[0])
        result = [['O'] * C for _ in range(R)]

        for r in range(R):
            for c in range(C):
                if g[r][c] == 'O':
                    result[r][c] = '.'
                    if r > 0:
                        result[r-1][c] = '.'
                    if r < R - 1:
                        result[r+1][c] = '.'
                    if c > 0:
                        result[r][c-1] = '.'
                    if c < C - 1:
                        result[r][c+1] = '.'
        return [''.join(row) for row in result]

    first = explode(grid)
    second = explode(first)

    if n % 4 == 3:
        return first
    else:
        return second


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
