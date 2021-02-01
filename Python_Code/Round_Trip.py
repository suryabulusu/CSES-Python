
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


import sys
from collections import defaultdict, deque
I = lambda : map(int, input().split())

sys.setrecursionlimit(10**8)

n, m = I()
adj = defaultdict(list)

for _ in range(m):
    a, b = I()
    adj[a].append(b)
    adj[b].append(a)

col = [None] * (n + 1)
par = [0] * (n + 1)

def dfs(u):
    col[u] = 1
    for v in adj[u]:
        if col[v] == 2: continue # its explored. done. 
        elif col[v] == 1 and v != par[u]:
            # wah backedge --> cycle
            path = []
            prev = u
            while True:
                path.append(prev)
                if v == par[prev]: break
                prev = par[prev]
            path.extend([v, u])
            print(len(path))
            print(*path)
            exit()

        elif col[v] is None: 
            col[v] = 1
            par[v] = u
            dfs(v)
            col[v] = 2


for i in range(1, n + 1):
    if col[i] == 2: continue
    col[i] = 1
    for u in adj[i]:
        par[u] = i
        dfs(u)  
        col[u] = 2
    col[i] = 2                 



print("IMPOSSIBLE")



# I once again ask you to try a few more times before referring here
