'''
Problem 4: Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import time


def largest_palindrome(num):
    num1 = num2 = pow(10,num) - 1

    ans_list = []
    for x in range(num1, pow(10,num-1), -1):
        for y in range(num2, pow(10,num-1), -1):
            ans = str(x * y)
            if ans == ans[::-1]:
                ans_list.append(int(ans))
    return max(ans_list)


if __name__ == '__main__':
    start_time = time.time()
    print(largest_palindrome(3))  # 906609
    print("--- %s seconds ---" % (time.time() - start_time))
