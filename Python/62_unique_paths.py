'''
This file implements the solution to the unique paths in a matrix problem. The DP is simple 2d.
dp[i][j] stores the number of unique paths to get to this position starting at the top left of the matrix.
dp[i][j] = dp[i-1][j] + dp[i][j-1]

Time Complexity: O(MN)
Space Complexity: O(MN)

Problem Link: https://leetcode.com/problems/unique-paths/
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        
        dp[m-1] = [1]*n
        
        # Base case
        for i in range(m):
            dp[i][n-1] = 1
        
        for c in range(n-2, -1, -1):
            for r in range(m-2, -1, -1):
                dp[r][c] = dp[r+1][c] + dp[r][c+1]
            
        return dp[0][0]