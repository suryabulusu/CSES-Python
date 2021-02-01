
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


# Z algorithm
S = input()
len_S = len(S)
z = [0] * (len_S)
l, r = 0, 0 
lens = []

for i in range(1, len_S):
    z[i] = max(0, min(z[i - l], r - i + 1)) # r - i + 1 can be neg?
    while (z[i] + i < len_S and (S[i + z[i]] == S[z[i]])): 
        z[i] += 1
        l, r = i, i + z[i] - 1 # r exceeds len_S
    
    if z[i] + i == len_S:
        lens.append(i)

# almost like borders code
print(*sorted(lens) + [len_S])



# I once again ask you to try a few more times before referring here
