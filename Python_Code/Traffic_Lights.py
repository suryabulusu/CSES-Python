
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


I = lambda : map(int, input().split())

n, x = I()

P = list(I())
arr = [0] + sorted(P) + [n, 0] # [0] added for empty slot

l = len(arr) - 1
adj = {arr[i]: [arr[i - 1], arr[i + 1]] for i in range(l)}

max_val = max(arr[i] - arr[i-1] for i in range(1, l))
bes = [max_val]
# note that the current state has all lights kept
# lets remove one by one
for p in P[::-1]:
    left, right = adj.pop(p)
    max_val = max(right - left, max_val) # if light at p was not there
    adj[left][1] = right
    adj[right][0] = left
    bes.append(max_val)

# print(adj)
print(*bes[::-1][1:]) # reverse and print



# I once again ask you to try a few more times before referring here
