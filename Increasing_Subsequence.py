
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


import bisect

n = int(input())

seq = [int(x) for x in input().split()]

sol = [1] * n # just the number itself

for i in range(1, n):
    for j in range(i): # almost like a search -- can do binsort?
        if seq[j] < seq[i]: sol[i] = max(sol[i], sol[j] + 1)

print(max(sol))

# I once again ask you to try a few more times before referring here
