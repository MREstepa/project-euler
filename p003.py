'''
Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import time


def largest_prime_factor(num):
    index = 2
    while index * index <= num:
        if num % index:
            index += 1
        else:
            num = num // index
    return num


if __name__ == '__main__':
    start_time = time.time()
    print(largest_prime_factor(600851475143))  # 6857
    print("--- %s seconds ---" % (time.time() - start_time))
