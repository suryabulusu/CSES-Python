
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


from collections import defaultdict

# help from : https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/dfs.py

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
vis = [False] * (n + 1)
fin = [False] * (n + 1)

def dfs(i): 

    stack = [i]
    while stack:
        u = stack[-1]

        if not vis[u]:
            vis[u] = True
            for v in adj[u]:
                if not vis[v]: 
                    stack.append(v)
        else:
            stack.pop()

            for v in adj[u]:
                if fin[v]: 
                    dp2[u] += max(dp1[v], dp2[v])

            for v in adj[u]:
                if fin[v]:
                    dp1[u] = max(dp1[u], 1 + dp2[v] + dp2[u] - max(dp1[v], dp2[v]))

            fin[u] = True

dfs(1)
print(max(dp1[1], dp2[1]))


# I once again ask you to try a few more times before referring here
