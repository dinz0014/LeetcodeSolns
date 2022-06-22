'''
This file implements the solution to the longest common subsequence problem. The dp array is structured in the following way:
dp[i][j] = The length of the longest common subsequence until ith index in text1 and jth index in text2
dp[i][j] = dp[i-1][j-1] + 1 if current characters match
dp[i][j] = max(dp[i][j-1], dp[i-1][j]) otherwise

Time Complexity: O(MN)
Space Complexity: O(MN)

Problem Link: https://leetcode.com/problems/longest-common-subsequence/
'''


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0]*n for _ in range(m)]
        
        for i in range(m):
            if i-1 >= 0 and dp[i-1][0] == 1:
                dp[i][0] = 1
            else:
                dp[i][0] = 1 if text1[i] == text2[0] else 0
        
        for i in range(n):
            if i-1 >= 0 and dp[0][i-1] == 1:
                dp[0][i] = 1
            else:
                dp[0][i] = 1 if text1[0] == text2[i] else 0
        
        for i in range(1, m):
            for j in range(1, n):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]