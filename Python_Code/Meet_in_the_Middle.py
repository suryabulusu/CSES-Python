
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


from itertools import combinations 
from collections import defaultdict

I = lambda : map(int, input().split())
n, s = I()

a = sorted(list(I()))

# if sum(a) < s: 
#     print(0)
#     exit()

def all_sums(arr):
    return [sum(x) for r in range(len(arr) + 1) for x in combinations(arr, r)]

s_a = all_sums(a[:len(a) // 2])
s_b = all_sums(a[len(a) // 2 :])

# print(s_a)
# print(s_b)

len_a = len(s_a)
cnt = 0
for idx, i in enumerate(s_b):
    k = 0
    b = len_a 
    while b > 0:
        while (k + b < len_a and i + s_a[k + b] <= s):
            k += b
        b = b // 2
    
    for v in range(k, -1, -1):
        # print(s_a[v], i, s, cnt)
        if s_a[v] + i != s: 
            break
        cnt += 1 
        
# # two pointer method - merge and stuff
# i, j = 0, 0
# # merge
# fin = []
# while i < len(s_a) and j < len(s_b):
#     if s_a[i] <= s_b[j]:
#         fin.append(s_a[i])
#         i += 1
#     elif s_a[i] > s_b[j]:
#         fin.append(s_b[j])
#         j += 1

# while i < len(s_a):
#     fin.append(s_a[i]); i += 1

# while j < len(s_b):
#     fin.append(s_b[j]); j += 1



print(cnt)

# I once again ask you to try a few more times before referring here
