
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

while True:
    l = 1 << p
    if l > n: break
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


q = int(input())
lex_keys = list(labs.keys())[:-1]

# print(lex_keys)

for _ in range(q):
    P = input()
    x, y = 0, n - 1
    for i in range(len(P)):
        l = n - 1
        k = x 
        while True:
            while (k + l <= y and i < len(lex_keys[k + l]) and lex_keys[k + l][i] <= P[i]):
                k += l
            l = l // 2 
            if l == 0: break
        y = k 

        l = n - 1
        while True:
            while (k - l >= x and i < len(lex_keys[k - l]) and lex_keys[k - l][i] >= P[i]):
                k -= l
            l = l // 2
            if l == 0: break
        
        x = k
        # print(x, y)

    if x == y:
        if P == lex_keys[x][:len(P)]: print("YES")
        else: print("NO")
    elif y - x + 1 > 0: print("YES")
    else: print("NO")
    


# I once again ask you to try a few more times before referring here
