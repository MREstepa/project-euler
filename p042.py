'''
Problem 42 Coded triangle numbers
The nth term of the sequence of triangle numbers is given by, 
tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its 
alphabetical position and adding these values we form a word value. 
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 
If the word value is a triangle number then we shall call the word 
a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K 
text file containing nearly two-thousand common English words, 
how many are triangle words?
'''

import os
import time

   
def coded_tri():
    with open(os.path.dirname(__file__) + '/data/p042.txt', 'r') as f:
        data = f.read()

    tri = [ int(((pow(num,2) + num) / 2)) for num in range(100) ]

    data = data.split(',')
    data = [x.strip('\"') for x in data]
    count = 0
    for rec in data:
        word = sum([(ord(char) - 96) for char in rec.lower()])
        if word in tri:
            count += 1

    return count


if __name__ == '__main__':
    start_time = time.time()
    print(coded_tri())  # 1786
    print("--- %s seconds ---" % (time.time() - start_time))
