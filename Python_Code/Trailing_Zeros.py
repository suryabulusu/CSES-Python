
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


n = int(input())

cnt, k = 0, 1
while True:
    if n < (5 ** k): break
    cnt += n // 5
    # 25 -> get added with 5 once, fir with 25
    k += 1
print(cnt)

#for i in range(1, n + 1):
    # n1 += fpow(i, 2) --> its obvious 5 hi hoga ffs
    # n2 += fpow(i, 5)

# I once again ask you to try a few more times before referring here
