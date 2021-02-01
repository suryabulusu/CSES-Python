
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


import typing

if __name__ == "__main__":
    firstline = input()
    n, m, k = [int(x) for x in firstline.split(" ")]
    secondline = input()
    a = [int(x) for x in secondline.split(" ")] # type: List[int]
    thirdline = input()
    b = [int(x) for x in thirdline.split(" ")] # type: List[int]

    a = sorted(a)
    b = sorted(b)

    i, j, cnt = 0, 0, 0

    while True:
        if b[j] >= a[i] - k and b[j] <= a[i] + k:
            cnt += 1
            i += 1
            j += 1
        elif b[j] < a[i] - k: j += 1
        elif b[j] > a[i] + k: i += 1

        if i == n or j == m: break

    print(cnt)

# I once again ask you to try a few more times before referring here
