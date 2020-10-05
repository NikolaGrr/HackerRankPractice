import math
import os
import random
import re
import sys
from collections import Counter

# Complete the minTime function below.
def minTime(n, machines, goal):
    counted_machine_dict = Counter(machines)
    fastest_machine = min(counted_machine_dict)
    min_days = 1
    max_days = math.ceil((fastest_machine * goal) / counted_machine_dict[fastest_machine])
    while max_days-min_days>1:
        mid = (min_days+max_days)//2
        output = sum((mid//key)*value for key,value in counted_machine_dict.items())
        if output<goal:
            min_days = mid
        else:
            max_days = mid
    return max_days

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nGoal = input().split()

    # n = int(nGoal[0])
    n = 50
    # goal = int(nGoal[1])
    goal = 306
    # machines = list(map(int, input().rstrip().split()))
    machines = [477, 448, 240, 858, 927, 703, 172, 68, 969, 943, 657, 499, 753, 777, 438, 199, 356, 435, 63, 292, 446, 164, 323, 511, 145, 607, 39, 832, 764, 692, 990, 240, 491, 581, 98, 769, 635, 621, 189, 603, 915, 197, 453, 667, 973, 890, 865, 328, 676, 928]
    ans = minTime(n, machines, goal)
    print(ans)
    # fptr.write(str(ans) + '\n')

    # fptr.close()