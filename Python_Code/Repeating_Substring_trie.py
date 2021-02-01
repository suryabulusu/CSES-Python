
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
        self.cnt = 0

    # private method
    def _c2i(self, c: str) -> int:
        return ord(c) - ord("a")

    def insert(self, key: str) -> bool:
        p = self.root
        cnt = 0
        for c in key:
            idx = self._c2i(c)
            if not p.children[idx]: 
                # self.cnt += 1
                p.children[idx] = TrieNode()
            else: 
                cnt += 1

            p = p.children[idx]
        p.isEnd = True
        if cnt > self.cnt:
            self.cnt = cnt
            return True

S = input()
n = len(S)
trie = Trie()
idx = 0
for i in range(n):
    if trie.insert(S[i:]): idx = i

if trie.cnt == 0: print("-1")
else: print(S[idx : idx + trie.cnt])

# I once again ask you to try a few more times before referring here
