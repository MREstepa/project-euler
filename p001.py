'''
Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

import time


def get_sum_of_multiples(num):
    multiples_list = [x for x in range(num) if x % 3 == 0 or x % 5 == 0]
    return sum(multiples_list)


if __name__ == '__main__':
    start_time = time.time()
    print(get_sum_of_multiples(1000))  # 233168
    print("--- %s seconds ---" % (time.time() - start_time))
