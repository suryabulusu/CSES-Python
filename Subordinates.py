
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)

n = int(input())

adj = defaultdict(list)

for idx, i in enumerate(list(map(int, input().split()))):
    adj[i].append(idx + 2) # directed

cnt = [0] * (n + 1)
vis = [False] * (n + 1)
# i know its a tree with root = 1
vis[1] = True

def dfs(i):
    for j in adj[i]:
        if not vis[j]:
            vis[j] = True
            dfs(j)
            cnt[i] += cnt[j] + 1

dfs(1)

print(*cnt[1:])

# I once again ask you to try a few more times before referring here
