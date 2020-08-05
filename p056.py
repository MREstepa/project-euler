'''
Problem 56 Powerful digit sum
A googol (10100) is a massive number: one followed by one-hundred zeros; 
100100 is almost unimaginably large: one followed by two-hundred zeros.
 Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, 
what is the maximum digital sum?
'''

import time

   
def powerful_digit():
    return max(
        [max([
            sum([int(z) for z in str(pow(x,k))]) for k in range(95,100)
        ]) for x in range(95,100)])


if __name__ == '__main__':
    start_time = time.time()
    print(powerful_digit())  # 972
    print("--- %s seconds ---" % (time.time() - start_time))
