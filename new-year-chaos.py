import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(n, q):
    # num_of_steps = 0
    # for i in list(range(n-1)):
    #     two_step_counter = 0
    #     num_of_checks = 0
    #     for j in list(range(i+1, n)):
    #         if q[i] > q[j]:
    #             num_of_steps += 1
    #             two_step_counter += 1
    #             num_of_checks += 1
    #         if two_step_counter > 2:
    #             return "Too chaotic"
    #         if num_of_checks > 7:
    #             break
    # return num_of_steps

    bribes = 0
    for i in range(n - 1, -1, -1):
            if q[i] - (i + 1) > 2:
                    print('Too chaotic')
                    return
            for j in range(max(0, q[i] - 2), i):
                    if q[j] > q[i]:
                            bribes += 1
    print(bribes)


if __name__ == '__main__':
    n = 5
    q = [2, 1, 5, 3, 4]
    minimumBribes(n, q)
