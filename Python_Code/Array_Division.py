
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


I = lambda : map(int, input().split())
n, k = I()
A = list(I())

l, r = max(A), sum(A)

def segment(max_val):
    cnt, cum_sum = 1, 0
    for x in A:
        if cum_sum + x <= max_val:
            cum_sum += x
        else:
            cum_sum = x 
            cnt += 1
    
    if cnt <= k: return (True, cnt)
    else: return (False, cnt) 

while (l <= r):
    mid = (l + r) // 2
    is_valid, segs = segment(mid)
    if is_valid: r = mid - 1
    else: l = mid + 1

    # print(l, r, mid, is_valid, segs)

print(r + 1)



# I once again ask you to try a few more times before referring here
