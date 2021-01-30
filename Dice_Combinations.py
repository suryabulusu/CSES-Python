
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


if __name__ == "__main__":
    n = int(input())
    sol = [1]
    # no need to maintain entire array.. just the previous six enough :/ 

    for i in range(1, n + 1):
        # sol.append(sum([sol[i - j] for j in range(1, 7) if i >= j]) % (10**9 + 7))
        sol += [sum(sol[-6:]) % (10 ** 9 + 7)]
    
    print(sol[n])


# I once again ask you to try a few more times before referring here
