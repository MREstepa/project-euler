'''
Problem 13: Large sum
Work out the first ten digits of the sum of the following 
one-hundred 50-digit numbers.
'''

import os
import time

    
def large_sum():
    with open(os.path.dirname(__file__) + '/data/p013.txt', 'r') as f:
        data = f.read()

    string = ''.join(data.split('\n'))
    string = list(map(''.join, zip(*[iter(string)]*50)))
    ans = 0
    for rec in string:
        ans += int(rec)
    return str(ans)[0:10]


if __name__ == '__main__':
    start_time = time.time()
    print(large_sum())  # 5537376230
    print("--- %s seconds ---" % (time.time() - start_time))
