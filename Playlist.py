
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


n = int(input())

# last = [-1] * (10**9)
last = {}
best = 0
start = 0
end = 0

for i in map(int, input().split()):
    end += 1
    if last.get(i, -1) >= start:
        start = last[i]
        
    last[i] = end
    
    best = max(best, end - start)

print(best)


# l = []
# best = 0
# for i in map(int, input().split()):
#     if i in l:
#         idx = l.index(i)
#         l = l[idx + 1 : ] + [i]
#     else: l += [i]
 
#     best = max(best, len(l))
 
# print(best)

# I once again ask you to try a few more times before referring here
