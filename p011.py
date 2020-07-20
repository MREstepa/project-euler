'''
Problem 11: Largest product in a grid
In the 20×20 grid below, four numbers along a diagonal line
 have been marked in red.

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same 
direction (up, down, left, right, or diagonally) in the 20×20 grid?
'''

import os
import time


def check_left_right(matrix, row, column):
    ans = 1
    for x in range(0,4):
        ans *= matrix[row][column + x]
    return ans

def check_up_down(matrix, row, column):
    ans = 1
    for x in range(0,4):
        ans *= matrix[row + x][column]
    return ans

def check_right_diag(matrix, row, column):
    ans = 1
    for x in range(0,4):
        ans *= matrix[row + x][column + x]
    return ans

def check_left_diag(matrix, row, column):
    ans = 1
    for x in range(0,4):
        ans *= matrix[row + x][column - x]
    return ans

def largest_product():
    with open(os.path.dirname(__file__) + '/texts/p011.txt', 'r') as f:
        data = f.read()

    matrix = []
    for x in range(20):
        # create matrix 
        row = []
        for y in range(20):
            row.append(int(data[0:2]))
            data = data[3:]
        matrix.append(row)
    
    max_prod = 0

    # left/right
    for x in range(0, 17):
        for y in range(0, 20):
            to_eval = check_left_right(matrix, y, x)
            if max_prod < to_eval:
                max_prod = to_eval

    # down/up
    for x in range(0,20):
        for y in range(0,17):
            to_eval = check_up_down(matrix, y, x)
            if max_prod < to_eval:
                max_prod = to_eval

    # diagonal right
    for x in range(0,17):
        for y in range(0,17):
            to_eval = check_right_diag(matrix, y, x)
            if max_prod < to_eval:
                max_prod = to_eval

    # diagonal left
    for y in range(0,17):
        for x in range (19, 2, -1):
            to_eval = check_left_diag(matrix, y, x)
            if max_prod < to_eval:
                max_prod = to_eval

    return max_prod


if __name__ == '__main__':
    start_time = time.time()
    print(largest_product())  # 70600674
    print("--- %s seconds ---" % (time.time() - start_time))
