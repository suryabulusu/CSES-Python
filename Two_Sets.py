
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


n = int(input())
tot = (n * (n + 1)) // 2

if tot & 1:
    print("NO")
    exit()

tot /= 2
a, b = [], []
for i in range(n, 0, -1):
    if i <= tot:
        a.append(i)
        tot -= i
    else: b.append(i)

print("YES")
print(len(a))
print(" ".join([str(i) for i in a]))
print(len(b))
print(" ".join([str(i) for i in b]))


# I once again ask you to try a few more times before referring here
