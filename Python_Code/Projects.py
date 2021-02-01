
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


from collections import defaultdict

# main idea from : https://codeforces.com/blog/entry/70018

n = int(input())

I = lambda : map(int, input().split())

all_days = []
ps, ev = [], []
m = 10 ** 6
for i in range(n):
    s, e, p = I()
    ps.append(p)
    ev.append((s, e))
    all_days.extend([m * (2*s) + i, m * (2*e + 1) + i])


all_days.sort()

# dp[i] -- paisa earned till day i
earn = defaultdict(int)
prev = 0
earn[0] = 0
for i, day in enumerate(all_days):
    idx = day % m
    day = day // m
    earn[day] = earn[prev] # earning is atleast same as prev day
    prev = day
    if day % 2:
        # if an end day - 
        earn[day] = max(earn[day], earn[ev[idx][0] * 2] + ps[idx])
        # meaning - what if you had instead worked only on this activity ending today

    # print(earn)

print(earn[all_days[-1] // m])









# I once again ask you to try a few more times before referring here
