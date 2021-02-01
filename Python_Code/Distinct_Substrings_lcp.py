
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


S = input()
n = len(S)
# prepare suffix array
p = 1
labs_prev = {}
labs_prev[""] = 0
for i in set(S): labs_prev[i] = ord(i) - ord("a") + 1

flag = 1
while flag:
    l = 1 << p
    if l >= n: 
        flag = 0
    p += 1

    # round1 
    labs = {}
    for i in range(0, n):
        s = S[i : i + l]
        a, b = s[ : l // 2], s[l // 2 : ]
        labs[s] = (labs_prev[a], labs_prev[b])
    
    # print("After round1: ", labs)
    # round2
    labs = sorted(labs.items(), key = lambda x: x[1])
    labs = {key : idx + 1 for idx, (key, val) in enumerate(labs)}
    labs[""] = 0 # empty string

    # print("After round1: ", labs)
    labs_prev = labs

# ref_suffix = {S[i:] : i for i in range(n)}

# suffix_arr = [None] * n
# for key, val in labs: suffix_arr[val] = ref_suffix[key]
labs_rev = {val : key for key, val in labs.items()}

# print(suffix_arr)

# lcp array prep
lcp = [0]
for i in range(n):
    if labs[S[i:]] == n: 
        lcp.append(0)
        continue 

    curr, nex = S[i:], labs_rev[labs[S[i:]] + 1]
    x = lcp[-1] - 1
    while True:
        if i + x < n and curr[x] == nex[x]: 
            x += 1
        else: break
    lcp.append(x)
    # print(lcp)


ans = (n * (n + 1)) // 2  - sum(lcp)
print(ans)







# I once again ask you to try a few more times before referring here
