
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


I = lambda : map(int, input().split())

n = int(input())
m = 10**9 + 7
modinv = lambda i: pow(i, m - 2, m)

# lets simply store values.. to keep track for entire program
MAX = 10**6
vals = [1] * (MAX + 1)
for i in range(2, MAX + 1): vals[i] = (vals[i - 1] * i) % m

for _ in range(n):
    a, b = I()
    res = (vals[a] * modinv(vals[a - b])) % m
    print(res, modinv(vals[b]))
    res = (res * modinv(vals[b])) % m
    print(res)


# I once again ask you to try a few more times before referring here
