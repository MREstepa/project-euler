'''
Problem 21: Amicable numbers
Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and 
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import math
import time

   
def proper_divisor(num):
    result = []
    i = 1
    while i <= num : 
        if (num % i==0) : 
            result.append(i)
        i = i + 1

    if num in result:
        result.remove(num)
    if result:
        return sum(result)
    else:
        return 0
    # return result  # to return list of proper divisors

def sum_amicable(num):
    ans = 0
    for x in range(4, num):
        if proper_divisor(proper_divisor(x)) == x and proper_divisor(x) != x:
            ans+=x

    return ans


if __name__ == '__main__':
    start_time = time.time()
    print(sum_amicable(10000))  # 31626
    print("--- %s seconds ---" % (time.time() - start_time))
