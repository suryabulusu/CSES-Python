
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


from itertools import accumulate    

I = lambda : map(int, input().split())

n, q = I()
a = list(accumulate(I()))
a = [0] + a

for _ in range(q):
    m, n = I()
    print(a[n] - a[m - 1])


# I once again ask you to try a few more times before referring here
