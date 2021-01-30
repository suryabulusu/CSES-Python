
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


from collections import defaultdict

I = lambda : map(int, input().split())

n = int(input())
adj = defaultdict(list)
for _ in range(n - 1):
    a, b = I()
    adj[a].append(b)
    adj[b].append(a)

# 2 dfs
depth = [0] * (n + 1)

def dfs(i):
    vis = [False] * (n + 1)
    stack = [i]
    while stack:
        u = stack[-1]
        if not vis[u]:
            vis[u] = True
            for v in adj[u]:
                if not vis[v]: 
                    stack.append(v)
                    depth[v] = depth[u] + 1
        else:
            stack.pop()


dfs(1)
b = depth.index(max(depth))
depth = [0] * (n + 1)
dfs(b)
print(max(depth))

# I once again ask you to try a few more times before referring here
