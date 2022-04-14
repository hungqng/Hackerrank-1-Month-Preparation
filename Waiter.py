#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def waiter(number, q):
    # Write your code here
    primegen = [1] * 10000
    prime = []
    
    for i in range(2, 10000):
        if primegen[i] == 1:
            for j in range(i, 10000, i):
                primegen[j] = 0
            prime.append(i)
    
    a = [[] for i in range(q + 1)]
    b = [[] for i in range(q + 1)]
    a[0] = number
    
    for i in range(q):
        while a[i]:
            plate = a[i].pop()
            if plate % prime[i] == 0:
                b[i + 1].append(plate)
            else:
                a[i + 1].append(plate)
    result = []
    
    for i in range(q + 1):
        while b[i]:
            result.append(b[i].pop())
            
    for i in range(q + 1):
        while a[i]:
            result.append(a[i].pop())
    return result
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()