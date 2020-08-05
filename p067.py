'''
Problem 67 Maximum path sum II
By starting at the top of the triangle below and moving to adjacent numbers 
on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 
'Save Link/Target As...'), a 15K text file containing a triangle with 
one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not 
possible to try every route to solve this problem, as there are 299 altogether!
 If you could check one trillion (1012) routes every second it would take over 
 twenty billion years to check them all. 
 There is an efficient algorithm to solve it. ;o)
'''

import os
import time


def triangle():
    with open(os.path.dirname(__file__) + '/data/p067.txt', 'r') as f:
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
    print(max_path())  # 7273
    print("--- %s seconds ---" % (time.time() - start_time))
