
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


n, a, b = map(int, input().split())

x = 6 * n
sol = [0] * (x + 1)
sol[0] = 1

for _ in range(n):
    for i in range(x, -1, -1):
        sol[i] = sum(sol[i - c] * (1/6) for c in range(1, 7) if i >= c)

    # print([(idx, round(i, 3)) for idx, i in enumerate(sol)])
    # print("******")

ans = 0
for i in range(a, b + 1):
    ans += sol[i]

print("%.6f" % ans)


# I once again ask you to try a few more times before referring here
