'''
Problem 28 Number spiral diagonals
Starting with the number 1 and moving to the right in a clockwise direction a 
5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
formed in the same way?
'''

import time


def diag_sum(num):
    ans, index = 1, 2
    diag_list = []

    while True:
        if ans == pow(num, 2):
            return sum(diag_list) + 1
        else:
            for x in range(4):
                ans += index
                diag_list.append(ans)
            index += 2
        

if __name__ == '__main__':
    start_time = time.time()
    print(diag_sum(1001))  # 669171001
    print("--- %s seconds ---" % (time.time() - start_time))
