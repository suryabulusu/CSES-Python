
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


I = lambda : map(int, input().split())

n, m = I()
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = I()
    adj[a].append(b) #directed

final_list = []
vis = [False] * (n + 1) 
fin = [False] * (n + 1)
for i in range(1, n + 1):
    if fin[i]: continue 
    stack = [i]
    while stack:
        # print(stack)
        u = stack[-1]
        if not vis[u]:
            vis[u] = True
            for v in adj[u]:
                # check for backedge
                if not vis[v]:
                    stack.append(v)
                else:
                    if not fin[v]:
                        print("IMPOSSIBLE her")
                        exit()
                
        else:
            stack.pop()
            # if u not in final_list: final_list.append(u) # things repeat in dfs stack
            if not fin[u]: final_list.append(u)
            fin[u] = True

if len(final_list) != n:
    print("IMPOSSIBLE th")
    print(final_list)
else: print(*final_list[::-1])

# I once again ask you to try a few more times before referring here
