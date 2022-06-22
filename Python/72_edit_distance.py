'''
This file implements the solution to the edit distance problem. Recursive solution with memoization is given here. We could make it better by implementing an iterative 
solution building the DP data bottom-up. 

The intuition is that we have two pointers track where we are upto, in matching the two words. (Say i and j)
If the characters at i and j match, we simply look at i+1 and j+1
Otherwise, we have 3 options:
1. Insert character into word1 such that word1[i-1] == word2[j]. Then, we move j to j+1 but keep i the same since we haven't removed/replaced the original character in word1
2. Replace word1[i] with word2[j]. Then, we increment both j and i by 1.
3. Delete word1[i]. Then, we increment i by 1.

Taking the minimum cost of the above 3 options gives us the minimum edit distance to turn word1[i:] into word2[j:]

Time Complexity: O(MN)
Storage Complexity: O(MN)

Problem Link: https://leetcode.com/problems/edit-distance/
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        
        def bfs(p, q):
            if (p,q) in dp:
                return dp[(p,q)]
            
            if p >= len(word1) and q >= len(word2):
                return 0
            
            if q >= len(word2):
                return len(word1) - p
            
            if p >= len(word1):
                return len(word2) - q
            
            if word1[p] == word2[q]:
                dp[(p,q)] = bfs(p+1,q+1)
                return dp[(p,q)]
            
            dp[(p,q)] = min(bfs(p, q+1), bfs(p+1,q), bfs(p+1,q+1)) + 1
            return dp[(p,q)]
        
        return bfs(0, 0)