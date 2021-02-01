
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


X = input()
Y = input()

n, m = len(X), len(Y)

dist = [[0] * (m + 1) for _ in range(n + 1)] 

for i in range(n + 1):
    for j in range(m + 1):
        if i == 0: dist[i][j] = j; continue 
        if j == 0: dist[i][j] = i; continue

        c = X[i - 1] != Y[j - 1] # won't reach when i or j = 0

        dist[i][j] = min(dist[i][j - 1] + 1, dist[i - 1][j] + 1, dist[i - 1][j - 1] + c)

print(dist[n][m])

# I once again ask you to try a few more times before referring here
