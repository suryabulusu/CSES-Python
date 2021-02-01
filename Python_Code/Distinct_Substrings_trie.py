
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

    def insert(self, key: str) -> None:
        p = self.root
        for c in key:
            idx = self._c2i(c)
            if not p.children[idx]: 
                self.cnt += 1
                p.children[idx] = TrieNode()
            p = p.children[idx]
        p.isEnd = True

S = input()
n = len(S)
trie = Trie()
for i in range(n // 10):
    trie.insert(S[i:])

print(trie.cnt)

# I once again ask you to try a few more times before referring here
