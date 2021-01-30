
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


if __name__ == "__main__":
    I = lambda : map(int, input().split())

    n, x = I()
    coins = sorted(I())

    sol = [1] + [0] * x

    # for c in coins:
    #     for i in range(c + 1, x + 1):
    #         sol[i] += sol[i - c] % (10 ** 9 + 7)
    # but this doesn't produce all permutations.. 

    for i in range(1, x + 1):
        for c in coins:
            if i < c: break
            sol[i] += sol[i - c] % (10 ** 9 + 7)
    
    print(sol[x] % (10 ** 9 + 7))

# I once again ask you to try a few more times before referring here
