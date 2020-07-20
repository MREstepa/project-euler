'''
Problem 48: Self powers
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

import time

   
def self_powers(num):
    ans = 0
    for x in range(1, num+1):
        ans += pow(x, x)
    return str(ans)[-10:]


if __name__ == '__main__':
    start_time = time.time()
    print(self_powers(1000))  # 9110846700
    print("--- %s seconds ---" % (time.time() - start_time))
