'''
Problem 39 Integer right triangles
If p is the perimeter of a right angle triangle with integral length sides, 
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

import time


def count_right_triangles(num): 
    perimeter = num
    store =[] 
  
    if perimeter % 2 != 0 : return 0
    else : 
        count = 0
        for b in range(1, perimeter // 2): 
  
            a = perimeter / 2 * ((perimeter - 2 * b) / (perimeter - b)) 
            inta = int(a) 
            if (a == inta ): 
                ab = tuple(sorted((inta, b))) 
                if ab not in store : 
                    count += 1
                    store.append(ab) 
        return count

def int_right_tri():
    max_perim = 0
    max_solution = 0
    for x in range(1000):
        count = count_right_triangles(x)
        if count != 0:
            if max_solution < count:
                max_solution = count
                max_perim = x
    return max_perim


if __name__ == '__main__':
    start_time = time.time()
    print(int_right_tri())  # 840
    print("--- %s seconds ---" % (time.time() - start_time))
