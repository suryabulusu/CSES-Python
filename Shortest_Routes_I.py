
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


from collections import defaultdict
import heapq

I = lambda : map(int, input().split())

n, m = I()
adj = defaultdict(list)

for _ in range(m):
    a, b, w = I()
    adj[a].append((b, w))

dist = [float("inf")] * (n + 1)
done = [False] * (n + 1)

dist[1] = 0
q = [] 
heapq.heappush(q, (dist[1], 1)) # dist, nodeID

while q:
    d_u, u = heapq.heappop(q)
    if done[u]: continue
    done[u] = True
    for (v, w_v) in adj[u]:
        if done[v]: continue
        # relax
        if d_u + w_v < dist[v]: 
            dist[v] = d_u + w_v
            heapq.heappush(q, (dist[v], v))

print(*dist[1:])





# I once again ask you to try a few more times before referring here
