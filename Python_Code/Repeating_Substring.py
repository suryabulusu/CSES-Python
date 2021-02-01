
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


S = input()

n = len(S)

# suffix array
# suff = [0] * n
lab = {}
for c in set(S): lab[c] = ord(c) - ord("a") + 1
lab[""] = 0

# print(lab)
p = 1
flag = 1
while flag:
    l = 1 << p
    if l >= n: 
        flag = 0
    p += 1

    curr_lab = []
    for i in range(n):
        # s1, s2 = S[i : i + l//2], S[i + l//2 : n]
        l1 = lab[S[i : i + l//2]]
        l2 = lab[S[i + l//2 : i + l]]
        curr_lab.append([S[i : i + l], (l1, l2)])

    curr_lab = sorted(curr_lab, key = lambda x: x[1])
    lab = {s[0] : idx + 1 for idx, s in enumerate(curr_lab)}
    lab[""] = 0 

    # print(lab)

# lcp array
lab_rev = {val : key for key,val in lab.items()}
lcp = [0]
for i in range(n):
    if lab[S[i:]] == n: 
        lcp.append(0)
        continue

    curr, nex = S[i:], lab_rev[lab[S[i:]] + 1]
    x = lcp[-1] - 1

    while i + x < n and curr[x] == nex[x]:
        x += 1
    lcp.append(x)



m = max(lcp)
i = lcp.index(m) - 1 
if m == 0:
    print("-1")
else: print(S[i : i + m]) 











# I once again ask you to try a few more times before referring here
