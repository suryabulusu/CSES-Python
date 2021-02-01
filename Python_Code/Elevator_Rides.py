
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


I = lambda : map(int, input().split())

n, x = I()
w = list(I())

tot = 1 << n

m = 10**9  
best = [m * (n + 1) + 0] * tot 
best[0] = m

for s in range(1, tot):
    for p in range(len(bin(s)[2:])):
        if (s & (1 << p)):
            k = best[s ^ (1 << p)]
            cnt, last = k // m, k % m 
            if last + w[p] <= x:
                last += w[p]
            else:
                cnt += 1
                last = w[p]
            best[s] = min(best[s], cnt*m + last)

print(best[tot - 1]//m)

# I once again ask you to try a few more times before referring here
