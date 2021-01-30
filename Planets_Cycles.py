
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


n = int(input())

# Floyd Algorithm
# explanation : https://stackoverflow.com/questions/2936213/explain-how-finding-cycle-start-node-in-cycle-linked-list-work
# few things to note in addition to ans: mu is the first time x_{mu + i} = x_{mu} occurs
# (having proved that i is multiple of cycle length L)

f = [0] * (n + 1)
idx = 1
for i in map(int, input().split()):
    f[idx] = i; idx += 1

memo = {}
ans = []
# 2 pointer tortoise hare method
for i in range(1, n + 1):
    if i in memo: 
        ans.append(memo[i])
        continue

    a, b = f[i], f[f[i]]
    while (a != b):
        a, b = f[a], f[f[b]]


    # first match obtained
    a = i
    till_cnt = 0 # coz we still at base
    while (a != b):
        a, b = f[a], f[b] # same speed
        till_cnt += 1
    first = a
    
    if first in memo:
        ans.append(memo[first] + till_cnt)
        continue

    #length of cycle
    b = f[a]
    cnt = 1 # one move made already
    while (a != b):
        b = f[b]
        cnt += 1

    fwd = i 
    for c in range(till_cnt):
        memo[fwd] = cnt + till_cnt - c
        fwd = f[fwd]


    for _ in range(cnt):
        memo[a] = cnt
        a = f[a]

    ans.append(memo[i]) # cnt + hops to reach count

# print(memo)
print(*ans)


# I once again ask you to try a few more times before referring here
