import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(n, arr):
    # num_of_swaps = 0
    # for i in list(range(n-1)):
    #     if arr[i] != i+1:
    #         index_swap = arr.index(i+1)
    #         arr[i], arr[index_swap] = arr[index_swap], arr[i]
    #
    #         num_of_swaps += 1
    # return num_of_swaps

    num_of_swap = 0
    index_dict = {value: index for index, value in enumerate(arr)}
    for i,v in enumerate(arr):
        correct_value = i+1
        if v != correct_value:
            index_to_swap = index_dict[correct_value]
            arr[index_to_swap], arr[i] = arr[i], arr[index_to_swap]
            index_dict[v] = index_to_swap
            index_dict[correct_value] = i
            num_of_swap +=1

    return num_of_swap


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
