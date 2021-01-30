
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


n = int(input())
x = list(map(int, input().split()))

best, prev = x[0], x[0]
for i in x[1:]:
    if i > prev + i: prev = i
    else: prev += i

    best = max(best, prev)    

print(best)


# I once again ask you to try a few more times before referring here
