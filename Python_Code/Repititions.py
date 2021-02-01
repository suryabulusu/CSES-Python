
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


if __name__ == "__main__":
    inp = input()
    cnt, maxcnt, prev = 1, 1, 0
    for i in inp:
        if i == prev:
            cnt += 1
        else:
            if cnt > maxcnt: maxcnt = cnt
            cnt = 1
            prev = i
    
    if cnt > maxcnt: maxcnt = cnt

    print(maxcnt)

# I once again ask you to try a few more times before referring here
