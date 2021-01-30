
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


S = input()
q = int(input())

for _ in range(q):
    P = input()
    # z-algo
    T = P + "#" + S
    len_T = len(T) 
    z = [0] * len_T 
    l, r = 0, 0
    flag = 0
    for i in range(1, len_T):
        z[i] = max(0, min(z[i - l], r - i + 1))
        while (z[i] + i < len_T and T[i + z[i]] == T[z[i]]):
            z[i] += 1
            l, r = i, i + z[i] - 1
        
        if z[i] == len(P):
            print("YES")
            flag = 1
            break
    
    if flag == 0: print("NO")



# I once again ask you to try a few more times before referring here
