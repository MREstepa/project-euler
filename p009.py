'''
Problem 9: Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import time


def pythagorean_triplet_generator() : 
    c, m = 0, 2
  
    while True: 
        for n in range(1, m) : 
            a = m * m - n * n 
            b = 2 * m * n 
            c = m * m + n * n 
  
            yield [a, b, c]

        m = m + 1
  
def special_pyth_triplet(num):
    pythagorean_triplet_gen = pythagorean_triplet_generator()

    while True:
        to_eval = next(pythagorean_triplet_gen)
        if to_eval[0] + to_eval[1] + to_eval[2] == 1000:
            return to_eval[0] * to_eval[1] * to_eval[2]


if __name__ == '__main__':
    start_time = time.time()
    print(special_pyth_triplet(1000))  # 23514624000
    print("--- %s seconds ---" % (time.time() - start_time))
