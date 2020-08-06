'''
Problem 104 Pandigital Fibonacci ends
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci 
number for which the last nine digits are 1-9 pandigital (contain all the 
digits 1 to 9, but not necessarily in order). And F2749, which contains 575 
digits, is the first Fibonacci number for which the first nine digits are 1-9 
pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits 
AND the last nine digits are 1-9 pandigital, find k.
'''

import time
import math


def fiboanacci_generator():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

def check_pandigital(num):
    num_str = ''.join([ x for x in sorted(str(num))])
    # pan = ''.join([str(x) for x in range(1,10)])
    return True if num_str == '123456789' else False

def pandigital_fib(): 
    fib_gen = fiboanacci_generator()

    x = next(fib_gen)
    count = 1
    while True:
        if check_pandigital(x % 1000000000):
            if check_pandigital(str(x)[:9]):
                return count
        count += 1
        x = next(fib_gen)


if __name__ == '__main__':
    start_time = time.time()
    print(pandigital_fib())  # 329468
    print("--- %s seconds ---" % (time.time() - start_time))
