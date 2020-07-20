'''
Number letter counts
  Show HTML problem content  
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
 in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 
342 (three hundred and forty-two) contains 23 letters and 
115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
'''

import time


def num999(n):
    ones = [
        "", "one ","two ","three ","four ", "five ", "six ","seven ",
        "eight ","nine ","ten ","eleven ","twelve ", "thirteen ", 
        "fourteen ","fifteen ","sixteen ","seventeen ", 
        "eighteen ","nineteen "
        ]
    twenties = [
        "","","twenty ","thirty ","forty ", "fifty ","sixty ",
        "seventy ","eighty ","ninety "
        ]
    
    c = n % 10
    b = ((n % 100) - c) / 10
    a = ((n % 1000) - (b * 10) - c) / 100
    t = ""
    h = ""
    if a != 0 and b == 0 and c == 0:
        t = ones[int(a)] + "hundred "
    elif a != 0:
        t = ones[int(a)] + "hundred and "
    if b <= 1:
        h = ones[n%100]
    elif b > 1:
        h = twenties[int(b)] + ones[int(c)]
    st = t + h
    return st
    
def num2word(num):
    thousands = [
        "","thousand ","million ", "billion ", "trillion ", 
        "quadrillion ", "quintillion ", "sextillion ", "septillion ",
        "octillion ", "nonillion ", "decillion ", "undecillion ", 
        "duodecillion ", "tredecillion ", "quattuordecillion ", 
        "quindecillion", "sexdecillion ", "septendecillion ", 
        "octodecillion ", "novemdecillion ", "vigintillion "
    ]

    if num == 0:
        return 'zero'
    i = 3
    n = str(num)
    word = ""
    k = 0
    while(i == 3):
        nw = n[-i:]
        n = n[:-i]
        if int(nw) == 0:
            word = num999(int(nw)) + thousands[int(nw)] + word
        else:
            word = num999(int(nw)) + thousands[k] + word
        if n == '':
            i = i+1
        k += 1
    return word[:-1]

def number_letter_count(num):
    ans = 0
    for x in range (1, num + 1):
        current = num2word(x)
        current = ''.join(current.split())
        ans += len(current)
    return ans


if __name__ == '__main__':
    start_time = time.time()
    print(number_letter_count(1000))  # 21113
    print("--- %s seconds ---" % (time.time() - start_time))
