'''
Problem 5: Smallest multiple

2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by 
all of the numbers from 1 to 20?
'''

import time


def prime_factors(num):
    i = 2
    factors = []
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return factors

def smallest_multiple(num):
    prime_fact_list = []
    for x in range(1, num+1):
        # get prime factor of 1-num
        prime_fact_list.append(prime_factors(x))

    max_pf = {}
    for pf_list in prime_fact_list:
        # add to dictionary with prime as key and power as value
        for rec in pf_list:
            max_pf.setdefault(rec,[]).append(pf_list.count(rec))

    ans_list = []
    for rec in max_pf:
        # add to list the prime raised to its highest power
        ans_list.append(pow(rec,max(max_pf[rec])))

    ans = 1
    for rec in ans_list:
        # multiply all values in the list
        ans *= rec

    return ans


if __name__ == '__main__':
    start_time = time.time()
    print(smallest_multiple(20))  # 232792560
    print("--- %s seconds ---" % (time.time() - start_time))
