
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################



I = lambda : map(int, input().split())
n = int(input())
cnt, maxcnt = 0, 0
t = []
for i in range(n):
    a, b = I()
    t.append(2 * a); t.append(2 * b + 1)

t.sort()

for p in t:
    if p & 1: cnt -= 1
    else: cnt += 1
    maxcnt = max(maxcnt, cnt)

print(maxcnt)

    


# I once again ask you to try a few more times before referring here
