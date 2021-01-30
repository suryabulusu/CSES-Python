
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


# sadly taking too much time :(

n = int(input())

I = lambda : map(int, input().split())

arr, dep = [], []

for _ in range(n):
    a, d = I()
    arr.append(a)
    dep.append(d)

ind_a = sorted(range(n), key = lambda i: arr[i])
ind_d = sorted(range(n), key = lambda i: dep[i])

# print(len(arr), len(dep))

cnt, maxcnt = 0, 0
room_assigned = [0] * n
i = 0
to_fill = list(range(n, 0, -1))
for idx, a in enumerate(ind_a):
    while dep[ind_d[i]] < arr[a]:
        cnt -= 1
        to_fill.append(room_assigned[ind_d[i]])
        # print(to_fill)
        i += 1

    cnt += 1

    room_assigned[a] = to_fill.pop()

    if cnt > maxcnt: maxcnt = cnt

print(maxcnt)

print(" ".join([str(i) for i in room_assigned]))

# I once again ask you to try a few more times before referring here
