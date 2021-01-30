
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################



# if someone's reading this -- just use PyPy3 for compilation
# and not CPython3
# PyPy3 uses JIT compilation which makes it super fast 
# https://stackoverflow.com/questions/59050724/whats-the-differences-python3-and-pypy3

I = lambda : map(int, input().split())

n, x = I()
coins = sorted(I())

sol = [0] + [10 ** 9] * x

# for i in range(1, x + 1):
#     sol[i] = min([sol[i - c] + 1 for c in coins if i >= c], default = 10 ** 9)
# map object coins drains out after one iter -- have to convert to list

f = [0] * (x + 1)

for c in coins:
    for i in range(c, x + 1):
        if sol[i - c] + 1 < sol[i]: 
            sol[i] = sol[i - c] + 1
            f[i] = c
        # sol[i] = min(sol[i], sol[i - c] + 1)


if sol[x] == 10 ** 9: print("-1")
else: 
    print(sol[x])
    
    # t = x
    # while True:
    #     print(f[t], end = " ")
    #     t -= f[t]
    #     if t == 0: break
    # if at all you want to print the solution


# I once again ask you to try a few more times before referring here
