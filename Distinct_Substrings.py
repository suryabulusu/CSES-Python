
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


#hashing
from collections import defaultdict
c2i = {c : ord(c) for c in "abcdefghijklmnopqrstuvwxyz"}
i2c = {i : c for c, i in c2i.items()}

A, B = 911382323, 972663749
S = input()
S_enc = [c2i[c] for c in S]
n = len(S)
h = [0] * n
p = [0] * n
p[0] = 1
h[0] = S_enc[0]
for i in range(1, n):
    h[i] = (h[i - 1] * A + S_enc[i]) % B 
    p[i] = (p[i - 1] * A) % B

def sub_hash(i, j):
    if i == 0: return h[j]

    return (h[j] - h[i - 1] * p[j - i + 1]) % B 

distinct = defaultdict(list)
for i in range(n):
    for j in range(i, n):
        # print(sub_hash(i, j))
        distinct[sub_hash(i, j)].append((i, j))

print(len(distinct.keys()))




# I once again ask you to try a few more times before referring here
