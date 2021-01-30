
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


if __name__ == "__main__":
    n = int(input())
    p = [int(x) for x in input().split()]
    tot = sum(p)
    
    minval = tot
    res = []

    def depth(k, minval):
        if k == n:
            return min(minval, abs(tot - 2 * sum(res)))
        else:
            minval = depth(k + 1, minval)
            res.append(p[k])
            minval = depth(k + 1, minval)
            del res[-1]

        return minval

    minval = depth(0, minval)
    print(minval)


# I once again ask you to try a few more times before referring here
