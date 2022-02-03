import math
import os
import random
import re
import sys


def longestIncreasingSubsequence(arr):
    lis =[]
    for i in range(len(arr)):
        lis.append(1)
    for i in range(len(arr)):
         for j in range(i):
                if arr[i]>arr[j] and lis[i]<lis[j]+1:
                    lis[i] += 1
    return max(lis)          
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = longestIncreasingSubsequence(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
