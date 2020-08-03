'''
Problem 34 Digit factorials
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial 
of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
'''

import time
import math


def digit_factorial():
    return sum([x for x in range(3, 41000) if sum([math.factorial(int(y)) for y in str(x)]) == int(x)])


if __name__ == '__main__':
    start_time = time.time()
    print(digit_factorial())  # 40730
    print("--- %s seconds ---" % (time.time() - start_time))
