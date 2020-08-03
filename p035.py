'''
Problem 35 Circular primes
The number, 197, is called a circular prime because all rotations of the digits: 
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

import time
import math


def is_prime(number):
    if number <= 1:
        return False

    for x in range(2, int(math.sqrt(number))):
        if not number % x:
            return False
    return True

def prime_generator():
    D = {}
    q = 2
    while 1:
        if q not in D:
            yield q
            D[q*q] = [q]

        else:
            for p in D[q]:
                D.setdefault(p+q,[]).append(p)
            del D[q]
        q += 1

def circular_primes():
    ans = 0

    prime_gen = prime_generator()
    x = next(prime_gen)
    while x < 1000000:
        x = next(prime_gen)
        shift = str(x)
        count = 0

        for y in range(len(shift)):
            shift = shift[-1] + shift[:-1]
            if is_prime(int(shift)):
                count += 1

        if count == len(shift):
            ans += 1
    return ans


if __name__ == '__main__':
    start_time = time.time()
    print(circular_primes())  # 40730
    print("--- %s seconds ---" % (time.time() - start_time))
