
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


s = input()
n = len(s)
m = 10**9 + 7

f = [1] * (n + 1)
for i in range(2, n + 1): f[i] = (f[i - 1] * i) % m

modinv = lambda x: pow(x, m - 2, m)
res = f[n]
for c in set(s):
    res = (res * modinv(f[s.count(c)])) % m

print(res)


# I once again ask you to try a few more times before referring here
