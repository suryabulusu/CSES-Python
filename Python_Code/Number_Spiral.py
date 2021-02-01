
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        y, x = (lambda : map(int, input().split()))()
        if x == y: print(x**2 + 1 - x)
        if y > x:
            if y % 2 == 0: print(y**2 - x + 1)
            else: print((y - 1)**2 + x)
        if x > y:
            if x % 2 == 1: print(x**2 - y + 1)
            else: print((x - 1)**2 + y)

# I once again ask you to try a few more times before referring here
