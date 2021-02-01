
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


# from collections import defaultdict
# # import sys

# # sys.setrecursionlimit(10**7)

n, m = map(int, input().split())


# # adj = defaultdict(list)

# # def add_edge(a, b):
# #     adj[a].append(b)
# #     adj[b].append(a)
arr = [['#']*(m+2)]+[list('#'+input()+'#') for _ in range(n)]+[['#']*(m+2)]

# arr = [["#"]*(m + 2) for _ in range(n + 2)]
# for i in range(1, n + 1):
#     arr[i][1:m+1] = list(input())
#     # for j, c in enumerate(input()):
#             # if j and arr[i][j - 1] == ".": add_edge(i*m + j, i*m + j - 1)
#             # if i and arr[i - 1][j] == ".": add_edge(i*m + j, i*m - m + j)
#         # arr[i][j + 1] = c
#             # add_edge(i*m + j, i*m + j) # self :(

# # vis = [False] * (n*m + m) 

# # def dfs(s):
# #     # if vis[s]: return

# #     vis[s] = True
# #     for u in adj[s]: 
# #         if not vis[u]: dfs(u)

# # for i in range(0, n + 2):
# #     print("".join(arr[i]))

cnt = 0
q = []

for i in range(1, n + 1):
    for j in range(1, m + 1):

        if arr[i][j] == ".":
        
#         # print(i, j)
            cnt += 1

            q.append((i, j))
            while q:
                a, b = q.pop()
                # print(a, b)
                arr[a][b] = "#"
                # del q[0]
                # for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
                for dx, dy in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                    if arr[a + dx][b + dy] == ".": 
                        q.append((a + dx, b + dy))
 
print(cnt)

# I once again ask you to try a few more times before referring here
