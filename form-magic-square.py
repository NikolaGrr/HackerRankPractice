import math
import os
import random
import re
import sys

def returnMagicSqares():
    init_magic_square = [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
    list_of_magic_squares = [init_magic_square]


    for iteration in list(range(3)):
        temp_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in list(range(3)):
            for j in list(range(3)):
                if i == 0:
                    if j == 0:
                        temp_matrix[0][2] = list_of_magic_squares[iteration][i][j]
                    elif j == 1:
                        temp_matrix[1][2] = list_of_magic_squares[iteration][i][j]
                    elif j == 2:
                        temp_matrix[2][2] = list_of_magic_squares[iteration][i][j]
                if i == 1:
                    if j == 0:
                        temp_matrix[0][1] = list_of_magic_squares[iteration][i][j]
                    elif j == 1:
                        temp_matrix[1][1] = 5
                    elif j == 2:
                        temp_matrix[2][1] = list_of_magic_squares[iteration][i][j]
                if i == 2:
                    if j == 0:
                        temp_matrix[0][0] = list_of_magic_squares[iteration][i][j]
                    elif j == 1:
                        temp_matrix[1][0] = list_of_magic_squares[iteration][i][j]
                    elif j == 2:
                        temp_matrix[2][0] = list_of_magic_squares[iteration][i][j]
        list_of_magic_squares.append(temp_matrix)

    # Transpose matrix
    for iteration in list(range(4)):
        temp_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in list(range(3)):
            for j in list(range(3)):
                if i == 0:
                    if j == 0:
                        temp_matrix[2][2] = list_of_magic_squares[iteration][i][j]
                    elif j == 1:
                        temp_matrix[1][2] = list_of_magic_squares[iteration][i][j]
                    elif j == 2:
                        temp_matrix[0][2] = list_of_magic_squares[iteration][i][j]
                if i == 1:
                    if j == 0:
                        temp_matrix[2][1] = list_of_magic_squares[iteration][i][j]
                    elif j == 1:
                        temp_matrix[1][1] = list_of_magic_squares[iteration][i][j]
                    elif j == 2:
                        temp_matrix[0][1] = list_of_magic_squares[iteration][i][j]
                if i == 2:
                    if j == 0:
                        temp_matrix[2][0] = list_of_magic_squares[iteration][i][j]
                    elif j == 1:
                        temp_matrix[1][0] = list_of_magic_squares[iteration][i][j]
                    elif j == 2:
                        temp_matrix[0][0] = list_of_magic_squares[iteration][i][j]
        list_of_magic_squares.append(temp_matrix)

    return list_of_magic_squares

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    magic_squares = returnMagicSqares()

    abs_difference = 1000
    for magic_square in magic_squares:
        curent_abs_difference = 0
        for i in list(range(3)):
            for j in list(range(3)):
                if s[i][j] != magic_square[i][j]:
                    curent_abs_difference += abs(s[i][j] - magic_square[i][j])
        if curent_abs_difference < abs_difference:
            abs_difference = curent_abs_difference

    return abs_difference

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

    #for _ in range(3):
    #    s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    #fptr.write(str(result) + '\n')

    #fptr.close()