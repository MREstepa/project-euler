'''
Problem 37 Truncatable primes
The number 3797 has an interesting property. Being prime itself, 
it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. 
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable 
from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

import time
import math


def is_prime(number):
    if number <= 1:
        return False

    for x in range(2, int(number)):
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

def truncatable_primes():
    count = 0
    ans = []
    prime_gen = prime_generator()

    for x in range(4):
        next(prime_gen)

    while True:
        rec = str(next(prime_gen))
        print(rec)
        x_count = 0
        l_rec = r_rec = rec
        for x in range(len(rec)):
            if is_prime(int(l_rec)) and is_prime(int(r_rec)):
                x_count += 1

            l_rec = l_rec[1:]
            r_rec = r_rec[:-1]
            if x_count == len(rec):
                count += 1
                ans.append(int(rec))
                print(rec, ans, sum(ans))
        if count == 11:
            return ans
    # return ans


if __name__ == '__main__':
    start_time = time.time()
    print(truncatable_primes())  # 748317
    print("--- %s seconds ---" % (time.time() - start_time))
