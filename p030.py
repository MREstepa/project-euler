'''
Problem 30 Digit fifth powers
Surprisingly there are only three numbers that can be written as the sum of 
fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers 
of their digits.
'''

import time


def digit_fifth():
    ans = []

    for x in range(2, 295246):
        x_list = [pow(int(y), 5) for y in str(x)]
        if x == sum(x_list):
            ans.append(x)

    return ans, sum(ans)


if __name__ == '__main__':
    start_time = time.time()
    print(digit_fifth())  # 443839
    print("--- %s seconds ---" % (time.time() - start_time))
