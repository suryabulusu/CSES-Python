
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


n = int(input())

tot, mx = 0, 0
for i in map(int, input().split()):
    tot += i
    mx = max(mx, i)

if mx > (tot - mx): print(2*mx)
else: print(tot) 


# I once again ask you to try a few more times before referring here
