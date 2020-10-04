import math
import os
import random
import re
import sys

# Complete the minTime function below.
def minTime(machines, goal):
    total = 0
    day = 0

    while total != goal:
        day += 1
        for machine in machines:
            if day % machine == 0:
                total += 1

    return day

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nGoal = input().split()

    # n = int(nGoal[0])
    n = 3
    # goal = int(nGoal[1])
    goal = 12
    # machines = list(map(int, input().rstrip().split()))
    machines = [4, 5, 6]
    ans = minTime(machines, goal)
    print(ans)
    # fptr.write(str(ans) + '\n')

    # fptr.close()