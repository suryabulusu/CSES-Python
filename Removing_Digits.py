
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


def digits(x):
    while True:
        yield x % 10
        x = x // 10
        if x == 0: break

n = int(input())

sol = [0] + [10 ** 9] * n
for i in range(1, min(10, n + 1)): sol[i] = 1

# f = [0] * (n + 1)
# for i in range(1, 10): f[i] = i

for i in range(10, n + 1):
    for j in digits(i):
        if sol[i - j] + 1 < sol[i]:
            sol[i] = sol[i - j] + 1
            # f[i] = j

print(sol[n])

# t = n
# while True:
#     print(t, end = "-->")
#     t -= f[t]
#     if t <= 0: break
# print("0")

# I once again ask you to try a few more times before referring here
