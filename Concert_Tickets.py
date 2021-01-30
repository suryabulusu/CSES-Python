
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


def find(i, s, e):
    c = (s + e) // 2
    if s >= e:
        if i >= h[c]:
            x = h[c]
            del h[c]
            return x
        else:
            return -1
        
    if i >= h[c]: ans = find(i, s, c)
    else: ans = find(i, c + 1, e)

    return ans

if __name__ == "__main__":
    I = lambda b: list(map(int, b.split()))
    # n, m = I()

    with open("test_input_concert.txt", "r") as f:
        lines = f.read().split("\n")
        n, m = I(lines[0])
        h = sorted(I(lines[1]))[::-1]

        p = I(lines[2])
    
    for i in p:
        if len(h) == 0: 
            print("-1")
            continue
        print(find(i, 0, len(h) - 1))
    



# I once again ask you to try a few more times before referring here
