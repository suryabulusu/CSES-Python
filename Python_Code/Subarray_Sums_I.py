
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


I = lambda : map(int, input().split())
n, t = I()
a = list(I()) 
s, e = 0, 0
cnt = 0
curr_sum = a[0]

while True:
    # print(s, e, curr_sum, cnt)
    if s >= n or e >= n: break
    if curr_sum == t:
        cnt += 1
        curr_sum -= a[s]
        s += 1
        e += 1
        if e < n: curr_sum += a[e]
    elif curr_sum < t:
        e += 1
        if e < n: curr_sum += a[e]
    elif curr_sum > t:
        curr_sum -= a[s]
        s += 1

print(cnt)

# I once again ask you to try a few more times before referring here
