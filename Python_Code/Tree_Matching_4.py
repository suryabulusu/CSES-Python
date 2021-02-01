
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


from collections import defaultdict
import sys
sys.setrecursionlimit(300000)

from types import GeneratorType
 
###
# solution from : RN2025	
# using yield for DFS
###
 
def iterative(f, stack=[]):
    def wrapped_func(*args, **kwargs):
        if stack: return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
                continue
            stack.pop()
            if not stack: break
            to = stack[-1].send(to)
        return to
 
    return wrapped_func
 

def inp(): return sys.stdin.readline().rstrip("\r\n")  # for fast input

 
def N():
    return int(inp())

def sep(): return map(int, inp().split())

def solve():
    
    @iterative
    def dfs(v,p):
        # print(f"v is {v+1} and p is {p+1}")
        # print(dp)
        # print(v,p)
 
        if len(g[v])==1 and g[v]==p :
            dp[v]=1
            yield
            return
 
        dp[v]=0
        for c in g[v]:
            if c==p:
                continue
            yield dfs(c,v)
            # print(f"v is {v+1} and p is {p+1}, c is {c+1}")
            # print(dp)
            dp[v]=dp[v]|dp[c]
        dp[v]=1-dp[v]
        yield
       
 
 
 
    n = N()
    g = [[] for _ in range(n)]
    for _ in range(n-1):
        a,b=sep()
        a-=1
        b-=1
        g[a].append(b)
        g[b].append(a)
    # print(g)
    dp = [0] * n
    dfs(0,-1)
 
 
    print(dp.count(0))
 
 
 
 
 
 
solve()


# I once again ask you to try a few more times before referring here
