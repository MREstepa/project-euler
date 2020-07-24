'''
Problem 16: Power digit sum
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
'''

import time

    
def power_digit(num1, num2):
    raised = pow(num1, num2)
    raised = [int(x) for x in str(raised)]
    
    return sum(raised)

if __name__ == '__main__':
    start_time = time.time()
    print(power_digit(2,1000))  # 1366
    print("--- %s seconds ---" % (time.time() - start_time))
