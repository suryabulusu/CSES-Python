
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


S = input()
n = len(S)

maxlen = (0, 0)
dp1 = [True] * n
dp2 = [False] * n 
for i in range(n - 1): 
    if S[i] == S[i + 1]:
        dp2[i + 1] = True
        maxlen = (1, i)
        
 
for l in range(2, n):
    dp_new = [False] * n
    for i in range(n - l):
        if dp1[i + l - 1]:
            if S[i] == S[i + l]: 
                dp_new[i + l] = True
                if l > maxlen[0]: maxlen = (l, i)
    dp1 = dp2
    dp2 = dp_new

print(S[maxlen[1] : maxlen[1] + maxlen[0] + 1])





# I once again ask you to try a few more times before referring here
