'''
Problem 80 Square root digital expansion
It is well known that if the square root of a natural number is not an integer,
 then it is irrational. The decimal expansion of such square roots is infinite 
 without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the
 first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums 
of the first one hundred decimal digits for all the irrational square roots.
'''

import decimal
import math
import time


def square(num):
    decimal.getcontext().prec = 101
    return sum(decimal.Decimal(num).sqrt().as_tuple()[1][:100]) \
        if not (int(math.sqrt(num) + 0.5) ** 2 == num) else 0


def digit_expansion(): 
    return sum([square(x) for x in range(100)]) - 1


if __name__ == '__main__':
    start_time = time.time()
    print(digit_expansion())  # 40886
    print("--- %s seconds ---" % (time.time() - start_time))
