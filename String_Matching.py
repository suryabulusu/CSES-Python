
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


import random

S = input()
P = input()
n, m = len(S), len(P)

c2i = lambda x: [ord(i) for i in x]

S, P = c2i(S), c2i(P)

# pattern matching with hash :)
# karp robin 
A, B = 911382323, 972663749
# preprocess
h = [0] * n
p = [0] * n 
h[0] = S[0]
p[0] = 1
for k in range(1, n):
    h[k] = (h[k - 1] * A + S[k]) % B
    p[k] = (p[k - 1] * A) % B

# pattern hash
p_hash = P[0]
for k in range(1, m):
    p_hash = (p_hash * A + P[k]) % B

# matching
def sub_hash(a, b):
    """computes hash of substring S[a....b] including j"""
    return (h[b] - h[a - 1] * p[b - a + 1]) % B

cnt = 0
for i in range(0, n - m + 1):
    j = i + m - 1
    if i == 0: s = h[j]
    else: s = sub_hash(i, j)

    if s == p_hash: 
        # additional check to avoid collisions
        idx = random.choice(range(i, j + 1))
        if S[idx] == P[idx - i]: cnt += 1
        # print(i, j)
        
print(cnt)

# I once again ask you to try a few more times before referring here
