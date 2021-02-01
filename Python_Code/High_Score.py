
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


from collections import defaultdict

I = lambda : map(int, input().split())

n, m = I()
edges = []
adj = defaultdict(list)

for _ in range(m):
    a, b, w = I()
    edges.append((a, b, w))
    adj[b].append(a) # for reachability check later on

dist = [-1 * float("inf")] * (n + 1)
dist[1] = 0
reachable = [False] * (n + 1)

for _ in range(n - 1):
    flag = 0
    for (a, b, w) in edges:
        if dist[a] + w > dist[b]:
            flag = 1
            dist[b] = dist[a] + w # ulta?

    if flag == 0:
        print(dist[n]); exit() # no point iterating further
    # print(dist)

# negative cycle [positive here]
last = []
for (a, b, w) in edges:
    if dist[a] + w > dist[b]: 
        dist[b] = dist[a] + w
        last.append(b)

# dfs run
stack = [n]
while stack:
    u = stack[-1]
    if not reachable[u]:
        reachable[u] = True
        if u in last:
            print(-1); exit()
        for v in adj[u]:
            if not reachable[v]:
                stack.append(v)
    else:
        stack.pop()

print(dist[n])

# I once again ask you to try a few more times before referring here
