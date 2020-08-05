'''
Problem 52 Permuted multiples
It can be seen that the number, 125874, and its double, 251748,
 contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, 
contain the same digits.
'''

import time

   
def permuted_multiple():
    x = 2
    while True:
        if ("".join(sorted(str(x)))) == ("".join(sorted(str(x * 2)))) \
                == ("".join(sorted(str(x * 3)))) == ("".join(sorted(str(x * 4)))) \
                == ("".join(sorted(str(x * 5)))) == ("".join(sorted(str(x * 6)))):
            return x
        x += 1


if __name__ == '__main__':
    start_time = time.time()
    print(permuted_multiple())  # 142857
    print("--- %s seconds ---" % (time.time() - start_time))
