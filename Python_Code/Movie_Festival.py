
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


I = lambda : map(int, input().split())
n = int(input())

t = []
for _ in range(n):
    a, b = I()
    t.append((a, b))

t = sorted(t, key = lambda x: x[1])

cnt = 0
endp = t[0][0]
for (a, b) in t:
    if a < endp: continue
    else:
        endp = b
        cnt += 1

print(cnt)


# I once again ask you to try a few more times before referring here
