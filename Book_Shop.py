
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


I = lambda : map(int, input().split())

n, x = I()
h = list(I()) # price of each book
s = list(I()) # pages of each book

# sol = [[0] * (n + 1) for _ in range(x + 1)]

# for i in range(1, x + 1):
#     for idx, j in enumerate(h):
#         t = 0
#         if i >= j: t = sol[i - j][idx] + s[idx]
#         sol[i][idx + 1] = max(sol[i][idx], t)

sol_2 = [0] * (x + 1)

for idx, price in enumerate(h):
    for i in range(x, price - 1, -1):
        sol_2[i] = max(s[idx] + sol_2[i - price], sol_2[i])

print(sol_2[x])


# I once again ask you to try a few more times before referring here
