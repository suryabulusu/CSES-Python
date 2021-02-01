
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


I = lambda : map(int, input().split())
n, x = I()
c = [(i + 1, j) for i, j in enumerate(I())]
c = sorted(c, key = lambda x: x[1])


found = False

# for idx, i in enumerate(c):
#     if i >= x: continue
#     if x - i in c:
#         if idx == c.index(x - i): continue
#         print(idx + 1, c.index(x - i) + 1)
#         found = True
#         break



i, j = 0, n - 1

while True:

    if i >= j: break

    if c[i][1] + c[j][1] == x:
        print(f"{c[i][0]} {c[j][0]}")
        found = True
        break
    elif c[i][1] + c[j][1] < x:
        i += 1
    else: j -= 1

if not found: print("IMPOSSIBLE")

# I once again ask you to try a few more times before referring here
