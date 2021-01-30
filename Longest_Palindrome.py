
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


# hashing -- slow and unnecessary - can do better with DP

S = input()
alph = "abcdefghijklmnopqrstuvwxyz"
c2i = {a : ord(a) for a in alph}
i2c = {ord(a) : a for a in alph}

A, B = 911382323, 972663749

S = [c2i[s] for s in S]
S_rev = S[::-1]
n = len(S)

h = [0] * n
h_rev = [0] * n
p = [0] * n 
h[0] = S[0]
h_rev[0] = S_rev[0]
p[0] = 1
for k in range(1, n):
    h[k] = (h[k - 1] * A + S[k]) % B
    h_rev[k] = (h_rev[k - 1] * A + S_rev[k]) % B
    p[k] = (p[k - 1] * A) % B

# print(h)
# print(h_rev)

def eq_subhash(a, b):
    a_rev, b_rev = n - 1 - b, n - 1 - a

    if a == 0: val1 = h[b]
    else: val1 = (h[b] - h[a - 1] * p[b - a + 1]) % B
    if a_rev == 0: val2 = h_rev[b_rev]
    else: val2 = (h_rev[b_rev] - h_rev[a_rev - 1] * p[b_rev - a_rev + 1]) % B

    # print(a, b, a_rev, b_rev, val1, val2)

    # mult1, mult2 = p[0], p[0]
    # if n - 1 > (a + b): mult2 = p[n - 1 - a - b]
    # else: mult1 =  p[a + b - n + 1]

    # val1 = (val1 * mult1) % B    
    # val2 = (val2 * mult2) % B

    # print(a, b, a_rev, b_rev, val1, val2)

    return (val1 == val2)

maxlen = 0
maxstr = ""
for i in range(n):
    for j in range(i, n):
        if eq_subhash(i, j):
            # print(i, j)
            if S[i] == S[j]: # additional check to avoid collision
                # print(i, j)
                if j - i + 1 > maxlen:
                    maxlen = j - i + 1
                    maxstr = "".join([i2c[s] for s in S[i:j+1]])

print(maxstr)




# I once again ask you to try a few more times before referring here
