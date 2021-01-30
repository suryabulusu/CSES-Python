
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


# Manacher's algorithm
# vibes of z-algorithm

S = input()
T = "|" + "".join(s + "|" for s in S)
n = len(T)
start =  0
maxlen = 0

hi, c = 0, 0
p = [0] * n

for r in range(n):
    l = 2 * c - r # c - l = r - c
    if hi > r:
        p[r] = min(p[l], hi - r) # z-algo like.. 
    else:
        p[r] = 0
    
    a = r + p[r] + 1
    b = r - p[r] - 1

    while b >= 0 and a < n and T[a] == T[b]:
        p[r] += 1
        b -= 1
        a += 1
    
    if r + p[r] > hi:
        # time to shift center
        c = r
        hi = r + p[r]

    if p[r] > maxlen:
        maxlen = p[r]
        start = r

# print(*p)
# print(T)

# print(start, maxlen)
print(T[start - maxlen + 1: start + maxlen : 2]) 
# start - maxlen + 1 -- coz border always has |
# start +  maxlen + 1 - 1 -- coz | at border

# I once again ask you to try a few more times before referring here
