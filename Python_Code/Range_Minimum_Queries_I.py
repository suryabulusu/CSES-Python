
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


I = lambda : map(int, input().split())
n, q = I()
a = list(I())

if n & (n - 1) != 0:
    # append values till it becomes power of 2
    p = len(bin(n)) - 2
    a += [max(a)] * (2**p - n)
    n = 2 ** p

# build segment tree
seg = [0] * n + a

def update(k, x):
    seg[k + n - 1] = x
    p = (k + n - 1) // 2
    while (p > 0):
        seg[p] = min(seg[2 * p], seg[2 * p + 1])
        p = p // 2

# build
for i in range(n - 1, 0, -1): 
    seg[i] = min(seg[i * 2], seg[i * 2 + 1])

def range_min(x, y):
    x += n - 1 
    y += n - 1

    min_val = seg[x] # just an init

    while (x <= y):
        if x % 2 == 1:
            min_val = min(min_val, seg[x])
            x += 1
        if y % 2 == 0:
            min_val = min(min_val, seg[y])
            y -= 1

        x = x // 2
        y = y // 2

    return min_val

# print(seg)

for _ in range(q):
    # k, x, y = I()
    # if k == 1:
    #     update(x, y)
    # else:
    #     print(range_min(x, y))

    x, y = I()
    print(range_min(x, y))


# I once again ask you to try a few more times before referring here
