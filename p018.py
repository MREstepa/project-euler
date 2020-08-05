'''
Problem 18 Maximum path sum I
By starting at the top of the triangle below and moving to adjacent 
numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

NOTE: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67, is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires
a clever method! ;o)
'''

import os
import time


def triangle():
    with open(os.path.dirname(__file__) + '/data/p018.txt', 'r') as f:
        data = [i.strip() for i in f.readlines()]
    tri = [[int(i) for i in rec.split(' ')] for rec in data]

    return tri

def max_path(): 
    tri = triangle()

    m = n = len(tri) - 1
    for i in range(m-1, -1, -1): 
        for j in range(i+1): 
  
            if (tri[i+1][j] > tri[i+1][j+1]): 
                tri[i][j] += tri[i+1][j] 
            else: 
                tri[i][j] += tri[i+1][j+1] 

    return tri[0][0] 


if __name__ == '__main__':
    start_time = time.time()
    print(max_path())  # 1074
    print("--- %s seconds ---" % (time.time() - start_time))
