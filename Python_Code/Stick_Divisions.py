
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


'''
https://usaco.guide/solutions/cses-1161?lang=cpp - idea credits
'''

import heapq

I = lambda : map(int, input().split())

x, n = I()
d = list(I())

# huffman coding
heapq.heapify(d)
# print(d)
cost = 0
while len(d) > 1:
    a = heapq.heappop(d)
    b = heapq.heappop(d)
    heapq.heappush(d, a + b)
    cost += a + b 

    # print(d)

print(cost)


# I once again ask you to try a few more times before referring here
