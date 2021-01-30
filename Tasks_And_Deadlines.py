
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


n = int(input())
I = lambda : map(int, input().split())

tot = 0
fin = []
for i in range(n):
    a, d = I()
    fin.append(a); tot += d

print(tot - sum([(idx + 1) * i for idx, i in enumerate(sorted(fin, reverse = True))]))



# I once again ask you to try a few more times before referring here
