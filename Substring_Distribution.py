
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


# have to speed it up.. 

S = input()
N = len(S)

# z-algo
def zmax(s):
    s = s[::-1]
    n = len(s)
    x, y = 0, 0
    z = [0] * n 
    max_z = 0
    for i in range(1, n):
        z[i] = max(0, min(z[i - x], y - i + 1))
        while (z[i] + i < n and s[z[i]] == s[i + z[i]]):
            z[i] += 1
            x, y = i, i + z[i] - 1
        
        if z[i] > max_z: max_z = z[i]
    # print(z)
    return max_z

dist = list(range(N, 0, -1))
for i in range(N):
    for j in range(zmax(S[:i + 1])): dist[j] -= 1

print(*dist)



# I once again ask you to try a few more times before referring here
