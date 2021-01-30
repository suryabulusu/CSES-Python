
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


alph = "abcdefghijklmnopqrstuvwxyz"
c2i = {a : ord(a) for a in alph}
i2c = {ord(a) : a for a in alph}

S = input()

A, B = 911382323, 972663749

S = S * 2
n = len(S)
S = [c2i[s] for s in S]
h = [0] * n
p = [0] * n 
h[0] = S[0]
p[0] = 1
for k in range(1, n):
    h[k] = (h[k - 1] * A + S[k]) % B
    p[k] = (p[k - 1] * A) % B

def sub_hash(a, b):
    if a == 0: return h[b]
    """computes hash of substring S[a....b] including j"""
    return (h[b] - h[a - 1] * p[b - a + 1]) % B

def ordering(s1, s2):
    # print("new call", s2)
    len_e = 0
    l = n // 4
    while l > 0:
        # print(l, len_e)
        # print(sub_hash(s1, s1 + len_e + l - 1) == sub_hash(s2, s2 + len_e + l - 1), s1, s1 + len_e + l - 1, s2, s2 + len_e + l - 1)
        while len_e + l <= n//2 and sub_hash(s1, s1 + len_e + l - 1) == sub_hash(s2, s2 + len_e + l - 1) and S[s1] == S[s2]: # addnal check for hash
            len_e += l
            # print(len_e, "***")
        l = l // 2

    if S[s1 + len_e] > S[s2 + len_e]: return s2
    else: return s1

    

min_idx = 0
for i in range(1, n - n//2):
    min_idx = ordering(min_idx, i)


print("".join([i2c[s] for s in S[min_idx : min_idx + n//2]]))



# I once again ask you to try a few more times before referring here
