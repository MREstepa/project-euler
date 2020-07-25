'''
Problem 8: Largest product in a series
The four adjacent digits in the 1000-digit number that have 
the greatest product are 9 × 9 × 8 × 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number 
that have the greatest product. What is the value of this product?
'''

import math
import os
import time


def greatest_adjacent():
    with open(os.path.dirname(__file__) + '/data/p008.txt', 'r') as f:
        data = f.read()

    string = ''.join(data.split('\n'))
    ans = []
    for x in range(len(string)-13):
        to_eval = string[:13]
        ans.append(math.prod([int(x) for x in to_eval]))
        string = string[1:]

    return max(ans)


if __name__ == '__main__':
    start_time = time.time()
    print(greatest_adjacent())  # 23514624000
    print("--- %s seconds ---" % (time.time() - start_time))

