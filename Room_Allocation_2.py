
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


# Solution via zdu863
# My solution failed coz i was sorting 2 lists
# one for arr and one for dep

n = int(input())

I = lambda : map(int, input().split())

arr = []
p = 10 ** 6 # why this .. aise hi?

for i in range(n):
    a, d = I()
    arr.extend([p * (2 * a) + i, p * (2 * d + 1) + i])

arr.sort()
res = [0] * n
to_fill = []
cnt = 0
for a in arr:
    pos = a % p
    val  = a // p

    if val % 2: to_fill.append(res[pos])
    elif to_fill:
        res[pos] = to_fill.pop()
    else:
        cnt += 1
        res[pos] = cnt

print(cnt)
print(*res)



# I once again ask you to try a few more times before referring here
