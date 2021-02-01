
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


n = int(input())
sol = [(0, 0)]
idx = 1
for i in map(int, input().split()):
    if i <= sol[-1][0]:
        while True:
            del sol[-1]
            if i > sol[-1][0]: break
    
    print(sol[-1][1], end = " ")
    
    sol.append((i, idx)); idx += 1

# by smaller -- he means strictly smaller

# I once again ask you to try a few more times before referring here
