
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


# s = input()
# t = "$" + "".join(c + '$' for c in s)
# n = 2 * len(s) + 1
# imaxpal = 0

# c = 0; r = 0; 
# p = [0] * n; 
# max_len = 0

# for i in range(n):
#     j = 2 * c - i
#     if r > i:
#         p[i] = min(r - i, p[j])
#     else:
#         p[i] = 0
 
#     a = i + (1 + p[i]); 
#     b = i - (1 + p[i])
 
#     while a < n and b >= 0 and t[a] == t[b]:
#             p[i] += 1; a += 1; b -= 1
 
#     if i + p[i] > r :
#         c = i
#         r = i + p[i]


#     if p[i] > max_len:
#         max_len = p[i]
#         imaxpal = i
 
# print(t[imaxpal-max_len+1:imaxpal+max_len:2])
 
S = input()
n = len(S)

lo, hi, maxlen = 0, 0, 0
start = 0
    
for c in range(1, n):
    
    lo, hi = c - 1, c
    while (lo >= 0 and hi < n and S[lo] == S[hi]): 
        if (hi - lo + 1) > maxlen:
            maxlen = hi - lo + 1
            start = lo
        hi += 1
        lo -= 1

    lo, hi = c - 1, c + 1
    while (lo >= 0 and hi < n and S[lo] == S[hi]): 
        if (hi - lo + 1) > maxlen:
            maxlen = hi - lo + 1
            start = lo
        hi += 1
        lo -= 1

print(S[start : start + maxlen])





# I once again ask you to try a few more times before referring here
