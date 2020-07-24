'''
Problem 14: Longest Collatz sequence
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) 
contains 10 terms. Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

import time

    
def longest_collatz(num):
    table = {}
    
    for x in range(1, num + 1):
        to_eval = x
        count = 1
        while to_eval != 1:
            if to_eval % 2:
                to_eval = (3 * to_eval) + 1
                if to_eval in table:
                    count += table[to_eval]
                    break
                else:
                    count += 1
            else:
                to_eval = to_eval / 2
                if to_eval in table:
                    count += table[to_eval]
                    break
                else:
                    count += 1
        table[x] = count
    return max(table, key=table.get)


if __name__ == '__main__':
    start_time = time.time()
    print(longest_collatz(1000000))  # 837799
    print("--- %s seconds ---" % (time.time() - start_time))
