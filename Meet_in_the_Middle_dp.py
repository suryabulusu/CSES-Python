
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


from itertools import combinations 

I = lambda : map(int, input().split())
n, s = I()

a = sorted(list(I()))

# knapsack
dp = [0] * (s + 1)
dp[0] = 1

for elem in a: # you want this above for knapsack -- this ensures dp_{k}[i] = dp_{k - 1}[i] + dp_{k - 1}[i - elem]
    for i in range(s, elem - 1, -1): # and reverse here -- 
        dp[i] += dp[i - elem] 
    # print(dp)


print(dp[s])


# I once again ask you to try a few more times before referring here
