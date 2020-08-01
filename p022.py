'''
Problem 22: Names scores
Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
 So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

import os
import time

   
def name_scores():
    with open(os.path.dirname(__file__) + '/data/p022.txt', 'r') as f:
        data = f.read()
    data = data.split(',')
    data = [x.strip('\"') for x in data]
    data.sort()

    return sum([
        (idx + 1) * sum([ord(char) - 96 for char in rec.lower()]) 
        for idx, rec in enumerate(data)
    ])

if __name__ == '__main__':
    start_time = time.time()
    print(name_scores())  # 871198282
    print("--- %s seconds ---" % (time.time() - start_time))
