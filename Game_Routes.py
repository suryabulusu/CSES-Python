
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


I = lambda : map(int, input().split())

n, m = I()
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = I()
    adj[a].append(b)

# make topsort
stack = [1]
vis = [False] * (n + 1)
fin = [False] * (n + 1)
f = []
while stack:
    u = stack[-1]
    if not vis[u]:
        vis[u] = True
        for v in adj[u]:
            stack.append(v)
    else:
        stack.pop()
        if not fin[u]: f.append(u)
        fin[u] = True
f = f[::-1]

# dp time
m = 10**9 + 7
ways = [0] * (n + 1)
ways[1] = 1 
for u in f:
    for v in adj[u]:
        ways[v] = (ways[v] + ways[u]) % m

print(ways[n] % m)

# I once again ask you to try a few more times before referring here
