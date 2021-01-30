
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


if __name__ == "__main__":
    n = int(input())

    if n in [2, 3]: print("NO SOLUTION")

    print(*range(2, n + 1, 2), *range(1, n + 1, 2))

# I once again ask you to try a few more times before referring here
