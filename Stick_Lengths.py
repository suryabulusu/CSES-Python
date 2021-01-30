
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


n = int(input())

l = sorted(list(map(int, input().split())))

m = l[len(l) // 2]

print(sum([abs(i - m) for i in l]))

# I once again ask you to try a few more times before referring here
