
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


I = lambda : map(int, input().split())

n, m = I()
edges = []
for _ in range(m):
    a, b, w = I()
    edges.append((a, b, w))

dist = [10**15] * (n + 1)
dist[1] = 0
p = [0] * (n + 1)
for _ in range(n - 1):
    flag = 0
    for (u, v, w) in edges:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            p[v] = u
            flag = 1

    if flag == 0:
        print("NO")
        exit()

for (u, v, w) in edges:
    if dist[u] + w < dist[v]:
        print("YES")
        p[v] = u
        i = v
        for _ in range(n):
            i = p[i]
        # now "i" is deffo part of cycle
        path = []
        start = i
        while True:
            path.append(i)
            if p[i] == start: break
            i = p[i]
        path.append(start)
        print(*path[::-1])
        exit()

print("NO")




# I once again ask you to try a few more times before referring here
