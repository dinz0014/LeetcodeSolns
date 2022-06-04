'''
This file implements the solution to the Longest Palindromic Substring problem. The idea is to check odd and even length palindromes considering each character
and the one next to it as potential palindromic centres.

Time Complexity: O(N^2) => expandCentre is potentially O(N) and we have 2N-1 centres
Storage Complexity: O(1) => We are not using any datastructures that depend on the input size

Problem Link: https://leetcode.com/problems/longest-palindromic-substring/
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expandCentre(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return right - left - 1
        
        if len(s) == 1:
            return s
        
        start, end = 0, 0
        
        for i in range(len(s)):
            oddLen = expandCentre(i, i)
            evenLen = expandCentre(i, i+1)
            bigLen = max(oddLen, evenLen)
            
            if bigLen > end - start:
                start = i - (bigLen - 1)//2
                end = i + bigLen//2
        
        return s[start:end+1]