
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


# from math import comb
# import operator as op
# from functools import reduce
# from math import factorial

# def comb(n, r):
    # r = min(r, n - r)
    # mult = op.mul
    # den = reduce(mult, range(1, r + 1), 1) # initial = 1
    # den = factorial(r) * factorial(n - r)
    # num = factorial(n)
    # num = reduce(mult, range(n, n - r, -1), 1)
    
    # return (num // den) % (10 ** 9 + 7)

n, k = map(int, input().split())
m = 10**9 + 7
res = n

if n == 1: print(1); exit()
if k == 1: print(n); exit()

modinv = lambda x: pow(x, m - 2, m)

for i in range(2, k + 1):
    den *= i % m
    num *= (n - 1 + i) % m
    res = (res * (n - 1 + i) * modinv(i)) % m

print(res)
 # py3.8 support not there in cses


# I once again ask you to try a few more times before referring here
