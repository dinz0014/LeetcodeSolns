'''
This file implements the solution to the maximum area of island problem. The solution is simple BFS to count number of grid squares that are connected and are marked 1.
Some optimisations include not keeping track of a visited set of coordinates and changing visited squares from 1 to 0 to avoid considering them in the future.

Time Complexity: O(MN)
Space Complexity: O(MN)

Problem Link: https://leetcode.com/problems/max-area-of-island/
'''

import collections
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        ans = 0
        q = collections.deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                
                area = 0
                q.append((i,j))
                # BFS from this square
                while q:
                    r, c = q.popleft()
                    
                    if grid[r][c] == 0:
                        continue
                    
                    # Change visited squares to 0 to indicate that they have already been visited
                    grid[r][c] = 0
                    area += 1
                    for dr, dc in dirs:
                        nr = r + dr
                        nc = c + dc
                        
                        if nr < 0 or nr >= m or nc < 0 or nc >= n:
                            continue
                        
                        if grid[nr][nc] == 1:
                            q.append((nr, nc))
                
                ans = max(area, ans)
        
        return ans