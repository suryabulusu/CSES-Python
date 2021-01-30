
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    print(pow(a, b, 10**9 + 7))

# I once again ask you to try a few more times before referring here
