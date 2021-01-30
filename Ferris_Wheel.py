
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


if __name__ == "__main__":
    # a better way to do -- 
    inp_func = lambda: map(int, input().split())

    n, x = inp_func()
    p = sorted(list(inp_func()))[::-1]

    j, g = n - 1, 0
    for i in range(n):
        if j < i: break 
        if p[i] <= x: 
            g += 1
            if p[i] + p[j] <= x: j -= 1

    print(g)    

# I once again ask you to try a few more times before referring here
