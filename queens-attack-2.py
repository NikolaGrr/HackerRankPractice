import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    att_fields = 0
    for obsticle in obstacles:
        r_o = obsticle[0]
        c_o = obsticle[1]

        if r_o == r_q:
            if c_o < c_q:
                att_fields += (c_q - c_o) - 1
                # att_fields += (n - c_q)
                # TODO: nije uzeto u obzir da prepreka moze da se nalazi sa obe strane
            elif c_o > c_q:
                att_fields += (c_o - c_q) - 1
                # att_fields += c_q - 1
                # TODO: nije uzeto u obzir da prepreka moze da se nalazi sa obe strane
        elif c_o == c_q:
            if r_o < r_q:
                att_fields += (r_q - r_o) - 1
                # att_fields += (n - r_q)
                # TODO: nije uzeto u obzir da prepreka moze da se nalazi sa obe strane
            elif r_o > r_q:
                att_fields += (r_o - r_q) - 1
                # att_fields += r_q - 1
                # TODO: nije uzeto u obzir da prepreka moze da se nalazi sa obe strane
        elif abs(r_q - r_o) == abs(c_q - c_o):
                att_fields += abs(r_q - r_o) - 1
                # TODO: nije uzeto u obzir da prepreka NE postoji
        # else:



    return att_fields


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nk = input().split()

    # n = int(nk[0])
    n = 5
    # k = int(nk[1])
    k = 3
    # r_qC_q = input().split()
    r_q, c_q = 4, 3
    # r_q = int(r_qC_q[0])
    #
    # c_q = int(r_qC_q[1])

    obstacles = [[5, 5], [4, 2], [2, 3]]

    # for _ in range(k):
    #     obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
