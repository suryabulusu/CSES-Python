
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


I = lambda : map(int, input().split())
n, m = I()

a = list(I())

f = lambda x: sum(x // i for i in a)

l, r = 1, m * max(a)
# ans = 0
while (l <= r):
    mid = (l + r) // 2 
    # print(l, r, mid, f(mid))  
    if f(mid) >= m:
        r = mid - 1
    elif f(mid) < m: l = mid + 1
    # elif f(mid) == m:
    #     print(mid)
    #     ans = 1; break

# print(l, r, mid, f(mid))

print(l)

# I once again ask you to try a few more times before referring here
