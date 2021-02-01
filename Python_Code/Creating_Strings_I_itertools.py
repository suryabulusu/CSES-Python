
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


from itertools import permutations

s = input()
res = set(permutations(s, len(s)))
print(len(res))
for i in sorted(set(res)):
    print("".join(i))

# I once again ask you to try a few more times before referring here
