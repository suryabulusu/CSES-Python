
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


n = int(input())

def pr(x):
    return 1 if x == "." else 0

mat = []
for _ in range(n):
    mat.append(list(map(pr, input())))

sol = [[0 for i in range(n)] for j in range(n)]
if mat[0][0] != 0: sol[0][0] = 1

for i in range(n):
    for j in range(n):
        if mat[i][j] == 0: continue

        if i >= 1: sol[i][j] += sol[i - 1][j] % (10 ** 9 + 7)
        if j >= 1: sol[i][j] += sol[i][j - 1] % (10 ** 9 + 7)

print(sol[n-1][n-1] % (10 ** 9 + 7))

# print(sol)


# I once again ask you to try a few more times before referring here
