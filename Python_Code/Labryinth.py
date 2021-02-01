
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


from collections import deque
n, m = map(int, input().split())

L_a, R_a = 0, 0
arr = [["#"]*(m + 2) for _ in range(n + 2)]
for i in range(1, n + 1):
    arr[i][1:m+1] = input()

f = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if arr[i][j] == "A": 
            L_a, R_a = i, j
            f = 1
            break
    if f == 1: break
    

q = deque([(L_a, R_a)])
ans = 0
L_b, R_b = 0, 0
text = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}
flag = 0
while q:
    x, y = q.popleft()
    for m, (dx, dy) in text.items():
        if arr[x + dx][y + dy] == ".":
            q.append((x + dx, y + dy))
            arr[x + dx][y + dy] = m
        if arr[x + dx][y + dy] == "B":
            print("YES")
            res = [m]
            while True: 
                if arr[x][y] == "A": break
                m = arr[x][y]
                res.append(m)
                dx, dy = text[m]
                x -= dx; y -= dy
            
            print(len(res))
            print("".join(res[::-1]))
            q = []
            flag = 1
            break

if flag == 0:
    print("NO")







# I once again ask you to try a few more times before referring here
