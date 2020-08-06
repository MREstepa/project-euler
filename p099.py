'''
Problem 99 Largest exponential
Comparing two numbers written in index form like 211 and 37 is not difficult, 
as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult, 
as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file 
containing one thousand lines with a base/exponent pair on each line, determine 
which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example 
given above.
'''

import time
import math
import os


def largest_exoponential(): 
    with open(os.path.dirname(__file__) + '/data/p099.txt', 'r') as f:
        data = [i.strip() for i in f.readlines()]
    exp = [[int(i) for i in rec.split(',')] for rec in data]
    index = ans = 0
    for idx, num in enumerate(exp):
        to_eval = math.log(num[0]) * num[1]
        if ans < to_eval:
            index = idx + 1
            ans = to_eval
    return index, ans


if __name__ == '__main__':
    start_time = time.time()
    print(largest_exoponential())  # 709
    print("--- %s seconds ---" % (time.time() - start_time))
