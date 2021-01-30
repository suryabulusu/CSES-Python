
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


I = lambda : map(int, input().split())

n, m = I()

adj = [[] for _ in range(n + 1)]
adj_rev = [[] for _ in range(n + 1)]
edges = []

for _ in range(m):
    a, b = I()
    adj[a].append(b) # children
    adj[b].append(a)
    edges.append((a, b, -1)) 

inf = 10**15
dist = [inf] * (n + 1)
dist[1] = 0
dist[n] = 0 # to ensure inf - 1 < inf situtation via n's parents
p = [0] * (n + 1)
# lets assume weights are -1
for _ in range(n - 1):
    flag = 0
    for (u, v, w) in edges:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w # relax
            p[v] = u
            flag = 1
    if flag == 0: break

if dist[n] == 0: 
    print("IMPOSSIBLE")
else: 
    print(dist[n] * -1 + 1)
    path = [n]
    while True:
        n = p[n]
        if n == 0: break
        else: path.append(n)
    print(*path[::-1])


# I once again ask you to try a few more times before referring here
