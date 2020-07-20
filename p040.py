'''
Problem 40: Champernowne's constant
An irrational decimal fraction is created by concatenating 
the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, 
find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

import time


def positive_int_generator():
    a = 1
    while True:
        yield a
        a += 1
   
def self_powers(num):
    posint_gen = positive_int_generator()

    string = ''
    while True:
        next_int = next(posint_gen)
        string += str(next_int)
        if len(string) >= 1000000:
            break
    index = 1
    ans = 1
    for x in range(7):
        ans *= int(string[index - 1])
        index *= 10
    return ans


if __name__ == '__main__':
    start_time = time.time()
    print(self_powers(1000))  # 210
    print("--- %s seconds ---" % (time.time() - start_time))
