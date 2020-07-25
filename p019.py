'''
Problem 19: Counting Sundays
You are given the following information, 
but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century 
unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century 
(1 Jan 1901 to 31 Dec 2000)?
'''

import datetime
import time

    
def sunday_count(date1, date2):
    year, month, date = date1.split('-')
    ans = 0
    for x in range((int(date2[:4]) - int(date1[:4])) + 1):
        for y in range(12):
            date_start = datetime.datetime.strptime(
                str(year) + '-' + str(y+1) + '-' + str(date), '%Y-%m-%d')
            if date_start.weekday() == 6:
                ans+=1
        year = int(year) + 1

    return ans


if __name__ == '__main__':
    start_time = time.time()
    print(sunday_count("1901-01-01", "2000-12-31"))  # 171
    print("--- %s seconds ---" % (time.time() - start_time))
