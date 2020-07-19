'''
Problem 6: Sum square difference
The sum of the squares of the first ten natural numbers is,

12+22+...+102=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)2=552=3025
Hence the difference between the sum of the squares of the 
first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum.
'''

import time


def sum_square_diff(num):
    sum_of_square = (num * (num + 1) * ((2 * num) + 1)) / 6
    square_of_sum = (pow(num, 2) * pow(num + 1, 2)) / 4

    return square_of_sum - sum_of_square

if __name__ == '__main__':
    start_time = time.time()
    print(sum_square_diff(100))  # 25164150
    print("--- %s seconds ---" % (time.time() - start_time))
