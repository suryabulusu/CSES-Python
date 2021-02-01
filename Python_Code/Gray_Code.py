
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


n = int(input())

g = ["0", "1"]
g_new = []
for i in range(1, n):
    g_new = ["0" + x for x in g]
    g_new += ["1" + x for x in g[::-1]]
    g = g_new 

print("\n".join(x for x in g))


# I once again ask you to try a few more times before referring here
