
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


col = [None] * (n + 1)
q = deque([1])
col[1] = 0
while q:
    u = q.popleft()
    for v in adj[u]:
        if col[v] is None:
            col[v] = (col[u] + 1) % 2
            # if all([col[u], col[v]]):
            #     m += 1
            #     col[u] = False; col[v] = False
            q.append(v)
            # else not an issue 
# print(i, m)
# max_m = max(m, max_m)
# print(col[1:])
# m = sum(col[1:])
# print(min(n - m, m))

# need to actually implement maxflow here :(                



# I once again ask you to try a few more times before referring here
