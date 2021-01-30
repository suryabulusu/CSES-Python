
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


from itertools import combinations

n = int(input())
tot = n * (n + 1) / 2

for r in range(1, n // 2 + 1):
    for sel in combinations(range(1, n + 1), r):
        if tot == 2 * sum(sel):
            print("YES")
            print(len(sel))
            print(" ".join([str(i) for i in sel]))
            print(n - len(sel))
            print(" ".join([str(i) for i in set(range(1, n + 1)).difference(sel)]))
            exit()

print("NO")

# I once again ask you to try a few more times before referring here
