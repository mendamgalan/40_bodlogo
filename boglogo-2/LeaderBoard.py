#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Create a sorted list of unique scores
    unique_scores = sorted(set(ranked), reverse=True)
    n = len(unique_scores)
    result = []
    index = n - 1  # Start from the end of unique_scores

    for score in player:
        while index >= 0 and score >= unique_scores[index]:
            index -= 1
        result.append(index + 2)  # +2 because index is 0-based and rank starts at 1

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
