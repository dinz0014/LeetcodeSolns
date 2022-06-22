'''
This file implements the solution to longest increasing path in matrix problem. Recursive with memoization is presented below. The idea is to go up,down,right and left
at each cell in matrix and pick the maximum at each recursive step.

Time Complexity: O(MN)
Storage Complexity: O(MN)

Problem Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
'''
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        m = len(matrix)
        n = len(matrix[0])
        
        def bfs(r, c):
            if (r,c) in dp:
                return dp[(r,c)]
            
            up, down, right, left = 0, 0, 0, 0
            
            if r+1 < m and matrix[r+1][c] > matrix[r][c]:
                down = bfs(r+1, c)
            if r-1 >= 0 and matrix[r-1][c] > matrix[r][c]:
                up = bfs(r-1, c)
            if c+1 < n and matrix[r][c+1] > matrix[r][c]:
                right = bfs(r, c+1)
            if c-1 >= 0 and matrix[r][c-1] > matrix[r][c]:
                left = bfs(r, c-1)
            
            dp[(r,c)] = 1 + max(up, down, right, left)
            return dp[(r,c)]
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, bfs(i, j))
        
        return ans