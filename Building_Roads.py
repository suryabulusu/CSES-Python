
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


from collections import defaultdict, deque
I = lambda : map(int, input().split())

n, m = I()
adj = defaultdict(list)

for _ in range(m):
    a, b = I()
    adj[a].append(b)
    adj[b].append(a)

# do bfs
vis = [False] * (n + 1)
sol = []

for i in range(1, n + 1):
    if not vis[i]:
        q = deque([i])
        sol.append(i)
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not vis[v]:
                    vis[v] = True
                    q.append(v)

print(len(sol) - 1)
for i, j in zip(sol[:-1], sol[1:]):
    print(i, j)

# I once again ask you to try a few more times before referring here
