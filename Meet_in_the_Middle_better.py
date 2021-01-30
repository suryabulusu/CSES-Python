
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


"""
Code mostly from user: nealzane 
"""
# from collections import defaultdict
I = lambda : map(int, input().split())
n, s = I()

def give_cnts(a):
    """returns cnts of the various sums that can occur using a <= s"""
    c = {0 : 1}
    for a_val in a:
        t = {}
        # don't want to update c directly in c.items() loop
        # hence creating another dict t
        for y, z in c.items():
            if a_val + y <= s: t[a_val + y] = z 
        for y, z in t.items():
            c[y] = c.get(y, 0) + z

    return dp

arr = list(I())

a = arr[0 : n//2]
b = arr[n//2 : ]

c = give_cnts(a)
d = give_cnts(b)

# print(c)
# print(d)

cnt = 0
for x, val in c.items():
    if s - x in d:
        cnt += d[s - x] * val
print(cnt) 


# I once again ask you to try a few more times before referring here
