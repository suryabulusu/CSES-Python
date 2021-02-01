
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


n = int(input())
coins = list(map(int, input().split()))

x = sum(coins)
sol = [1] + [0] * x


print(coins)
for c in sorted(coins):
    for i in range(c, x + 1):
        sol[i] += sol[i - c]
    print(sol)

print(len([1 for i in sol if i > 0]))

# print(sol)

for i in range(1, x + 1):
    if sol[i] != 0: print(i, end = " ")

# I once again ask you to try a few more times before referring here
