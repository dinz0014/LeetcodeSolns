'''
This file implements the Python solution for leetcode problem 208. More specifically, it implements a trie data structure that supports insert, search and prefix search
features. The time complexity for insert is O(M), for search is O(M) and for prefix search is also O(M).

Problem link: https://leetcode.com/problems/implement-trie-prefix-tree/
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        
        curr.isEnd = True                
    
    def search(self, word: str) -> bool:
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                return False
            
            curr = curr.children[c]
        
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for c in prefix:
            if c not in curr.children:
                return False
            
            curr = curr.children[c]
        
        return True
