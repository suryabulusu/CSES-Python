
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


# z-algorithm 
# idea from : https://cp-algorithms.com/string/z-function.html#toc-tgt-8

S = input()

def z_max(s):
    n = len(s)
    z = [0] * n
    x, y = 0, 0
    maxz = 0
    for i in range(1, n):
        z[i] = max(0, min(z[i - x], y - i + 1))
        while (z[i] + i < n and s[i + z[i]] == s[z[i]]):
            z[i] += 1
            x, y = i, i + z[i] - 1

        maxz = max(maxz, z[i])

    return maxz

cnt = 0
for i in range(len(S)):
    cnt += (i + 1 - z_max(S[ : i + 1]))
    # print(cnt)

print(cnt)



        




# I once again ask you to try a few more times before referring here
