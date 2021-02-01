
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


from collections import defaultdict
import sys, threading
import resource
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**7)
# threading.stack_size(32768 * 64)

# def solve():
I = lambda : map(int, input().split())

n = int(input())
adj = defaultdict(list)
for _ in range(n - 1):
    a, b = I()
    adj[a].append(b)
    adj[b].append(a)

# O(V) algo thanks to dp
dp1 = [0] * (n + 1)
dp2 = [0] * (n + 1)
# vis = [False] * (n + 1) -- no need to maintain vis[] for tree, coz no cycle

def dfs(u, p): # p = parent

    for v in adj[u]:
        if v == p: continue
        dfs(v, u)
        dp2[u] += max(dp1[v], dp2[v]) # u not in matching

    # let dp2[u] reach its final form -- then we can update dp1
    for v in adj[u]:
        if v == p: continue
        dp1[u] = max(dp1[u], 1 + dp2[v] + dp2[u] - max(dp1[v], dp2[v])) # u in matching..wah 
        # print(u, dp1[u], dp2[u])

# choose any node to start
# vis[1] = True
dfs(1, 0)

# print(*dp1)
# print(*dp2)

print(max(dp1[1], dp2[1]))

# threading.Thread(target=solve).start()

# I once again ask you to try a few more times before referring here
