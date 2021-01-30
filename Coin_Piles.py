
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


I = lambda : map(int, input().split())
t = int(input())

for _ in range(t):
    a, b = I()
    K1 = (2 * a - b)
    K2 = (2 * b - a)

    if K1 >= 0 and K2 >= 0: 
        if K1 % 3 == 0 and K2 % 3 == 0:
            print("YES")
            continue
    print("NO")


# I once again ask you to try a few more times before referring here
