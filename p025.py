'''
Problem 25: 1000-digit Fibonacci number
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence 
to contain 1000 digits?
'''

import time


def fiboanacci_generator():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b
   
def first_term_index(num):
    fibonacci_gen = fiboanacci_generator()
    count = 0
    while True:
        to_eval = next(fibonacci_gen)
        count += 1
        if len(str(to_eval)) == num:
            return count


if __name__ == '__main__':
    start_time = time.time()
    print(first_term_index(1000))  # 4782
    print("--- %s seconds ---" % (time.time() - start_time))
