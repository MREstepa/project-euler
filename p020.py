'''
Problem 20: Factorial digit sum
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

import time


def factorial(num):
    if num == 1:
        return num
    elif num < 1:
        return ("NA")
    else:
        return num * factorial(num - 1)
   
def factorial_digit_sum(num):
    expanded = factorial(num)
    expanded = [x for x in str(expanded)]
    ans = 0
    for rec in expanded:
        ans += int(rec)
    return ans


if __name__ == '__main__':
    start_time = time.time()
    print(factorial_digit_sum(100))  # 1366
    print("--- %s seconds ---" % (time.time() - start_time))
