
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


if __name__ == "__main__":
    num = input()
    I = lambda : map(int, input().split())
    p = list(I())
    c, pr = 0, 0
    for i in range(len(p)):
        if p[i] < pr: c += pr - p[i]
        else: pr = p[i]
    
    print(c)

# I once again ask you to try a few more times before referring here
