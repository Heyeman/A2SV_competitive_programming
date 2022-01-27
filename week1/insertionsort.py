#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for i in range(1,len(arr)):
        j = i
        tmp = 0
        while j > 0 and arr[j] < arr[j-1]:
            tmp = arr[j]
            arr[j] = arr[j-1]
            for k in arr:
                print(k, end = ' ')
            print('')
            arr[j-1] = tmp
            j -= 1
    for k in arr:
                print(k, end = ' ')
            
                

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
