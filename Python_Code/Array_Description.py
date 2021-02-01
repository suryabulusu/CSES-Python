
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


I = lambda : map(int, input().split())

n, m = I()
x = list(I())

dp = [0 for _ in range(m + 2)]
if x[0] == 0: dp = [0] + [1] * m + [0]  
else: dp[x[0]] = 1

M = 10**9 + 7
# print(dp)
for i in range(1, n):
    dp_new = [0 for _ in range(m + 2)]
    if x[i] == 0:
        for j in range(1, m + 1):
            dp_new[j] = (dp[j - 1] + dp[j] + dp[j + 1]) % M
    else:
        dp_new[x[i]] = (dp[x[i] - 1] + dp[x[i]] + dp[x[i] + 1]) % M 

    # print(dp_new)
    dp = dp_new

print(sum(dp) % M)



        





# I once again ask you to try a few more times before referring here
