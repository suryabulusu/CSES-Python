
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


# RUNTIME ERROR -- RECURSION DEPTH LIMIT EXCEEDED

if __name__ == "__main__":
    n = int(input())
    tot = sum(range(1, n + 1))
    
    res = []

    def depth(k):
        if k == n + 1:
            if tot == 2 * sum(res):
                print("YES")
                print(len(res))
                print(" ".join([str(i) for i in res]))
                not_in_res = set(range(1, n + 1)).difference(res)
                print(len(not_in_res))
                print(" ".join([str(i) for i in not_in_res]))
                exit() # NOT AT ALL A GOOD WAY BUT KYA HI KAR SAKTE :(
        else:
            depth(k + 1)
            res.append(k)
            depth(k + 1)
            del res[-1]

        return 

    depth(1)

    print("NO")


# I once again ask you to try a few more times before referring here
