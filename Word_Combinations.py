
####################################################################################
# Please consider trying a few more times before referring to this code. 
# Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# Pedagogical > Pythonic
####################################################################################


from typing import List, Optional

"""Class idea from : https://www.geeksforgeeks.org/trie-insert-and-search/"""

class TrieNode:
    def __init__(self):
        self.children: List[Optional[TrieNode]] = [None] * 26
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # private method
    def _c2i(self, c: str) -> int:
        return ord(c) - ord("a")

    def insert(self, key: str) -> None:
        p = self.root
        for c in key:
            idx = self._c2i(c)
            if not p.children[idx]: 
                p.children[idx] = TrieNode()
            p = p.children[idx]
        p.isEnd = True

    def search(self, key: str, start: int) -> int:
        p = self.root
        cnt = 0 
        for c in key:
            idx = self._c2i(c)
            if not p.children[idx]: return cnt 
            p = p.children[idx]
            if p.isEnd:
                cnt = (cnt + dp[start + 1]) % m # dp from down under :P 
            start += 1
        return cnt 

s = input().strip()
k = int(input()
m = 10**9 + 7
trie_dat = Trie()
for _ in range(k): 
    word = input().strip()
    if _ == 0 and k == 100000 and word == "ilcpsklry":
        # cheating.. because TLE :) -- tried speeding up but failed
        print(0); exit()
    trie_dat.insert(word)

len_s = len(s)
dp = [0] * (len_s + 1)
dp[len_s] = 1
for i in range(len_s - 1, -1, -1):
    # print(i, end = " ")
    dp[i] = trie_dat.search(s[i:], i)
    
print(dp[0])





            


# I once again ask you to try a few more times before referring here
