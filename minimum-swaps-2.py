import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(n, arr):
    num_of_swaps = 0
    for i in list(range(n-1)):
        if arr[i] != i+1:
            index_swap = arr.index(i+1)
            arr[i], arr[index_swap] = arr[index_swap], arr[i]

            num_of_swaps += 1
    return num_of_swaps

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input())

    #arr = list(map(int, input().rstrip().split()))
    m = 2
    n = [7, 4]
    arr = [[1, 3, 5, 2, 4, 6, 7], [4, 3, 1, 2]]
    for i in list(range(m)):
        res = minimumSwaps(n[i], arr[i])
        print(res)
    #fptr.write(str(res) + '\n')

    #fptr.close()
