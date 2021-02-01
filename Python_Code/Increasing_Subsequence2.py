
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


import bisect

n = int(input())

sol = []

for i in map(int, input().split()):
    if not sol: sol.append(i)
    else:
        if i > sol[-1]: sol.append(i)
        else:
            # replace elem in sol[] that is just
            # greater than i
            idx = bisect.bisect_left(sol, i)
            sol[idx] = i

    # print(sol)

print(len(sol))


# I once again ask you to try a few more times before referring here
