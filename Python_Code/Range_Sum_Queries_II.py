
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


I = lambda : map(int, input().split())
n, q = I()
a = list(I())

# fenwick tree -- 1-indexed
bit = [0] * (n + 1) 

def update(x, k):
    while (k <= n):
        bit[k] += x
        k += k & -k # jump till upper 2^k reaches

# sum from 1..k
def sum(k):
    if k == 0: return 0
    res = 0
    while (k >= 1):
        res += bit[k]
        k -= k & -k # jump till lower 2^k reaches
    return res

# prepare fenwick
for idx, i in enumerate(a): update(i, idx + 1)

# print(bit)

for _ in range(q):
    k, x, y = I()
    if k == 1:
        update(y - a[x - 1], x)
        a[x - 1] = y
    else:
        print(sum(y) - sum(x - 1))





# I once again ask you to try a few more times before referring here
