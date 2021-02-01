
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


from collections import defaultdict
S = input()
len_S = len(S)
char_cnts = defaultdict(int)
for s in S: char_cnts[s] += 1

res = ""
if len_S % 2: # odd
    flag = 0
    for key, val in char_cnts.items():
        if val % 2:
            if flag == 0:
                flag = 1
                cent = key
                res += key * ((val - 1) // 2)
            else: 
                print("NO SOLUTION")
                exit()
        else:
            res += key * (val // 2) 
    res = res + cent + res[::-1]
else: 
    for key, val in char_cnts.items():
        if val % 2:
            print("NO SOLUTION")
            exit()
        else:
            res += key * (val // 2)
    res = res + res[::-1]

print(res)



# I once again ask you to try a few more times before referring here
