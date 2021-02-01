
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


# from collections import defaultdict
from heapq import heappop, heappush # another cosmetic change -- import heapq --> to this

I = lambda : map(int, input().split())

n, m = I()
edges = []
adj = [[] for _ in range(n + 1)]
adj_rev = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, w = I()
    # edges.append([a, b, w]) # -- don't store faltu extra stuff
    # [but srsly, terrible that using bit of extra space is bad. bc python]
    adj[a].append((b, w))
    adj_rev[b].append((a, w))

infty = 10**15
dist_1 = [infty] * (n + 1)
dist_n = [infty] * (n + 1)
def dijkstra(g, d, start):
    
    # done = [False] * (n + 1)
    d[start] = 0
    q = [(d[start], start)] # changed from q = []; heappush(q, ()) ..wah
    while q:
        d_u, u = heappop(q)
        if d_u == d[u]: # attained its final state :)
            for (v, w_v) in g[u]:
                if d_u + w_v < d[v]: 
                    d[v] = d_u + w_v
                    heappush(q, (d[v], v))
        # if done[u]: continue
        # done[u] = True
        # for (v, w_v) in g[u]:
        #     if done[v]: continue
        #     if d_u + w_v < d[v]: 
        #         d[v] = d_u + w_v
        #         heappush(q, (d[v], v))

    #return d --> having a return is bit expensive

min_dist = infty
dijkstra(adj, dist_1, start = 1)
dijkstra(adj_rev, dist_n, start = n)

for u in range(1, n + 1): # wrote range(n + 1) earlier which led to TLE for 1 case. wah python
    for (v, w) in adj[u]:
        min_dist = min(dist_1[u] + w // 2 + dist_n[v], min_dist)

print(min_dist)


### BF
# dist_1 = [float("inf")] * (n + 1)
# dist_1[1] = 0
# for _ in range(n - 1):
#     flag = 0
#     for [u, v, w] in edges:
#         if dist_1[v] > dist_1[u] + w:
#             dist_1[v] = dist_1[u] + w
#             flag = 1
#     if flag == 0: break

# dist_n = [float("inf")] * (n + 1)
# dist_n[n] = 0
# for _ in range(n - 1):
#     flag = 0
#     for [v, u, w] in edges: # reverse v, u 
#         if dist_n[v] > dist_n[u] + w:
#             dist_n[v] = dist_n[u] + w
#             flag = 1
#     if flag == 0: break

# I once again ask you to try a few more times before referring here
