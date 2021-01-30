
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
    if i > r:
        cnt = 0
        while True:
            if (cnt < len_S - i) and (S[i + cnt] == S[cnt]): cnt += 1
            else: break
        z[i] = cnt
        l, r = i, i + z[i] - 1
    else:
        # r - i + 1 = len after i till r
        if z[i - l] < r - i + 1:
            z[i] = z[i - l]
        else:
            z[i] = r - i + 1
            while True:
                if (z[i] < len_S - i) and (S[i + z[i]] == S[z[i]]): z[i] += 1
                else: break
            l, r = i, i + z[i] - 1
            # repeating lines.. but this makes more sense algo wise..
            # pedagogical :P 

    # border part
    if z[i] + i == len_S:
        lens.append(z[i])

# print(*z)
print(*sorted(lens))



# I once again ask you to try a few more times before referring here
