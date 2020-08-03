'''

Problem 24 Lexicographic permutations
A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, 
we call it lexicographic order.  The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

from itertools import permutations 
import time


def permutation_generator(num):
    perm = permutations([x for x in range(num)])

    for rec in list(perm):
        yield rec

def lexi_perm(num):
    perm = permutation_generator(10)

    for x in range(num - 1):
        next(perm)
    return ''.join([str(x) for x in next(perm)])


if __name__ == '__main__':
    start_time = time.time()
    print(lexi_perm(1000000))  # 2783915460
    print("--- %s seconds ---" % (time.time() - start_time))
