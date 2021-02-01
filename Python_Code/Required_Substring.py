
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


# Some help from : https://github.com/mrsac7/CSES-Solutions/blob/master/src/1112%20-%20Required%20Substring.cpp
# Idea came from searching a lot really
# tough one :(

n = int(input())
S = input()
m = len(S)

# border array compute
b = [0] * m
for i in range(1, m):
    k = b[i - 1] # S[0...k-1] = S[i-1-k...i-1]
    while (k != 0 and S[k] != S[i]):
        k = b[k - 1]
    # either k = 0 or S[k] == S[i]
    if S[k] == S[i]:
        b[i] = k + 1 

# print(b)

# dfa next state compute
trans = [[0] * 26 for _ in range(m)]
for s in range(m):
    for c in range(26):
        if c == ord(S[s]) - ord("A"):
            trans[s][c] = s + 1
        else:
            trans[s][c] = trans[b[s - 1]][c] # b[s-1] imp!!! not b[s]

# print(trans)

# now dp
dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 1

M = 10**9 + 7
for i in range(1, n + 1):
    for j in range(m):
        for c in range(26):
            dp[i][trans[j][c]] += dp[i - 1][j]
            dp[i][trans[j][c]] %= M
            # print(i, j, c)

# print(dp)

# take example "AA" and n = 4
# AA$$, $AA$, $$AA - fill dollars with chars
# however AAAA kinda repeats in all if u use all chars

tot = pow(26, n, M)
for j in range(m):
    tot -= dp[n][j]
    tot %= M

print(tot)




# I once again ask you to try a few more times before referring here
