
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


# import sys
from collections import defaultdict, deque
I = lambda : map(int, input().split())

# sys.setrecursionlimit(10 ** 8)

n, m = I()
adj = defaultdict(list)

for _ in range(m):
    a, b = I()
    adj[a].append(b)
    adj[b].append(a)

# bipartite - dfs

# def dfs(i, c):

#     for u in adj[i]:
#         if col[u] is not None:
#             col[u] = c
#             dfs(u, (c + 1) % 2)
#         else:
#             if col[u] != c:
#                 print("IMPOSSIBLE")
#                 exit()

col = [None] * (n + 1)
for i in range(1, n + 1):
    if col[i] is None:
        q = deque([i])
        col[i] = 0
        while q:
            u = q.popleft()
            c = col[u]
            for v in adj[u]:
                if col[v] is None:
                    col[v] = (c + 1) % 2
                    q.append(v)
                else:
                    if col[v] == c:
                        print("IMPOSSIBLE")
                        exit()
        # dfs(i, (c + 1) % 2)
        

print(*[i + 1 for i in col[1:]])

# I once again ask you to try a few more times before referring here
