'''
Problem 7: 10001st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

import time


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

def nth_prime(num):
    prime_gen = prime_generator()
    for rec in range(num):
        ans = next(prime_gen)
    return ans


if __name__ == '__main__':
    start_time = time.time()
    print(nth_prime(10001))  # 104743
    print("--- %s seconds ---" % (time.time() - start_time))
