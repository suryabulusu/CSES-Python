
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


from collections import defaultdict, deque

I = lambda : map(int, input().split())

n = int(input())
adj = defaultdict(list)
for _ in range(n - 1):
    a, b = I()
    adj[a].append(b)
    adj[b].append(a)

# run bfs V times
max_m = 0
for i in range(1, n + 1):
    col = [None] * (n + 1)
    m = 0
    q = deque([i])
    col[i] = True
    while q:
        u = q.popleft()
        for v in adj[u]:
            if col[v] is None:
                col[v] = True
                if all([col[u], col[v]]):
                    m += 1
                    col[u] = False; col[v] = False
                q.append(v)
                # else not an issue 
    # print(i, m)
    max_m = max(m, max_m)

print(max_m)
                



# I once again ask you to try a few more times before referring here
