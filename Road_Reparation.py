
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

edges = sorted(edges, key = lambda x: x[2])

# kruskal - union find structure
link = [i for i in range(n + 1)]
size = [1 for i in range(n + 1)] 

def find(x):
    while True:
        if link[x] == x: break
        else: x = link[x]
    return x 

final_wt = 0
edge_cnt = 0
for (a, b, w) in edges:
    rep_a = find(a)
    rep_b = find(b)
    if rep_a == rep_b: continue

    if size[rep_a] > size[rep_b]:
        rep_a, rep_b = rep_b, rep_a # swap
    link[rep_a] = rep_b
    size[rep_b] += size[rep_a]

    final_wt += w
    edge_cnt += 1

if edge_cnt == n - 1: # tree
    print(final_wt)
else: print("IMPOSSIBLE")




# I once again ask you to try a few more times before referring here
