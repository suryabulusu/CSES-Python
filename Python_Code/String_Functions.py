
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


S = input()
n = len(S)

# z-algo
z = [0] * n
x, y = 0, 0
for i in range(1, n):
    z[i] = max(0, min(z[i - x], y - i + 1))
    while (z[i] + i < n and S[i + z[i]] == S[z[i]]):
        z[i] += 1
        x, y = i, i + z[i] - 1
print(*z)

# border array
b = [0] * n # border array
for i in range(1, n):
    k = b[i - 1]
    while (k > 0 and S[k] != S[i]):
        k = b[k - 1]
    
    if S[k] == S[i]:
        b[i] = k + 1
    else: b[i] = 0
print(*b)




# I once again ask you to try a few more times before referring here
