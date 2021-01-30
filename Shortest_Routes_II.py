
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


# from collections import defaultdict
# import heapq

I = lambda : map(int, input().split())

n, m, q = I()
# adj = defaultdict(list)
adj = [[float("inf")]*(n+1) for _ in range(n + 1)]

for i in range(1, n + 1): adj[i][i] = 0

for _ in range(m):
    a, b, w = I()
    # adj[a].append((b, w))
    w = min(w, adj[a][b])
    adj[a][b] = w
    adj[b][a] = w

# floyd warshall.. 
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            adj[i][j] = min(adj[i][k] + adj[k][j], adj[i][j])

for _ in range(q):
    i, j = I()
    if adj[i][j] == float("inf"): print(-1)
    else: print(adj[i][j])

# I once again ask you to try a few more times before referring here
