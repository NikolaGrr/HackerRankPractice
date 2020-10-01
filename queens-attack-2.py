import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    att_fields_r_plus = 10000
    att_fields_r_minus = 10000
    att_fields_c_plus = 10000
    att_fields_c_minus = 10000
    att_fields_diagonal_r_minus_c_minus = 10000
    att_fields_diagonal_r_minus_c_plus = 10000
    att_fields_diagonal_r_plus_c_minus = 10000
    att_fields_diagonal_r_plus_c_plus = 10000
    for obsticle in obstacles:
        r_o = obsticle[0]
        c_o = obsticle[1]

        if r_o == r_q:
            if c_q > c_o:
                att_fields_c_minus = min(att_fields_c_minus, abs(c_q - c_o) - 1)
            elif c_q < c_o:
                att_fields_c_plus = min(att_fields_c_plus, abs(c_q - c_o) - 1)
        elif c_o == c_q:
            if r_q > r_o:
                att_fields_r_minus = min(att_fields_r_minus, abs(r_q - r_o) - 1)
            elif r_q < r_o:
                att_fields_r_plus = min(att_fields_r_plus, abs(r_q - r_o) - 1)
        elif abs(r_q - r_o) == abs(c_q - c_o):
            if r_q > r_o and c_q > c_o:
                att_fields_diagonal_r_minus_c_minus = min(att_fields_diagonal_r_minus_c_minus, abs(r_q - r_o) - 1)
            if r_q > r_o and c_q < c_o:
                att_fields_diagonal_r_minus_c_plus = min(att_fields_diagonal_r_minus_c_plus, abs(r_q - r_o) - 1)
            if r_q < r_o and c_q > c_o:
                att_fields_diagonal_r_plus_c_minus = min(att_fields_diagonal_r_plus_c_minus, abs(r_q - r_o) - 1)
            if r_q < r_o and c_q < c_o:
                att_fields_diagonal_r_plus_c_plus = min(att_fields_diagonal_r_plus_c_plus, abs(r_q - r_o) - 1)

    # Provera ukoliko prepreka ne postoji
    if att_fields_r_plus == 10000:
        att_fields_r_plus = n - r_q
    if att_fields_r_minus == 10000:
        att_fields_r_minus = r_q - 1
    if att_fields_c_plus == 10000:
        att_fields_c_plus = n - c_q
    if att_fields_c_minus == 10000:
        att_fields_c_minus = c_q - 1
    if att_fields_diagonal_r_minus_c_minus == 10000:
        if c_q > r_q:
            att_fields_diagonal_r_minus_c_minus = r_q - 1
        elif c_q < r_q:
            att_fields_diagonal_r_minus_c_minus = c_q - 1
        elif c_q == r_q:
            att_fields_diagonal_r_minus_c_minus = c_q - 1
    if att_fields_diagonal_r_minus_c_plus == 10000:
        if n - c_q > r_q - 1:
            att_fields_diagonal_r_minus_c_plus = r_q - 1
        elif n - c_q < r_q - 1:
            att_fields_diagonal_r_minus_c_plus = n - c_q
        elif n - c_q == r_q - 1:
            att_fields_diagonal_r_minus_c_plus = n - c_q
    if att_fields_diagonal_r_plus_c_minus == 10000:
        if n - r_q > c_q - 1:
            att_fields_diagonal_r_plus_c_minus = c_q - 1
        elif n - r_q < c_q - 1:
            att_fields_diagonal_r_plus_c_minus = n - r_q
        elif n - r_q == c_q - 1:
            att_fields_diagonal_r_plus_c_minus = n - r_q
    if att_fields_diagonal_r_plus_c_plus == 10000:
        if c_q > r_q:
            att_fields_diagonal_r_plus_c_plus = n - c_q
        elif c_q < r_q:
            att_fields_diagonal_r_plus_c_plus = n - r_q
        elif c_q == r_q:
            att_fields_diagonal_r_plus_c_plus = n - r_q

    return att_fields_r_plus + att_fields_r_minus + att_fields_c_plus + att_fields_c_minus + att_fields_diagonal_r_minus_c_minus + att_fields_diagonal_r_minus_c_plus + att_fields_diagonal_r_plus_c_minus + att_fields_diagonal_r_plus_c_plus


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
