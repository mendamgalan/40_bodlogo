#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    n = len(container)
    
    container_sums = [sum(row) for row in container]
    type_sums = [sum(container[i][j] for i in range(n)) for j in range(n)]
    if sorted(container_sums) == sorted(type_sums):
        return "Possible"
    else:
        return "Impossible"

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
