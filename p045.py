'''
Problem 45 Triangular, pentagonal, and hexagonal
Triangle, pentagonal, and hexagonal numbers are generated by the 
following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''

import math
import time

   
def is_pentagonal(num): 
    num = (1 + math.sqrt(24 * num + 1)) / 6
    return( (num - int (num)) == 0) 

def is_hexagonal(num): 
    val = 8 * num + 1
    x = 1 + math.sqrt(val) 
    num = x / 4

    return True if ((num - int(num)) == 0) else False

def tri_pent_hex():
    x = 286
    while True:
        y = int(((pow(x,2) + x) / 2))
        if is_pentagonal(y) and is_hexagonal(y):
            return y
        else:
            x += 1


if __name__ == '__main__':
    start_time = time.time()
    print(tri_pent_hex())  # 1533776805
    print("--- %s seconds ---" % (time.time() - start_time))
