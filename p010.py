'''
Problem 10: Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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

def sum_prime(num):
    prime_gen = prime_generator()
    prime = next(prime_gen)

    ans = 0
    while prime < num:
        ans += prime
        prime = next(prime_gen)

    return ans


if __name__ == '__main__':
    start_time = time.time()
    print(sum_prime(2000000))  # 142913828922
    print("--- %s seconds ---" % (time.time() - start_time))
