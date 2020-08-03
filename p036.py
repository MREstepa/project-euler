'''
Problem 36 Double-base palindromes
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic 
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include 
leading zeros.)
'''

import time


def double_base():
    return sum([x for x in range(1000000) if str(x) == str(x)[::-1] and format(x, 'b') == format(x, 'b')[::-1]])


if __name__ == '__main__':
    start_time = time.time()
    print(double_base())  # 872187
    print("--- %s seconds ---" % (time.time() - start_time))
