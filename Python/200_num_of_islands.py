'''
This file implements the solution to number of islands leetcode problem. The idea is to do BFS from each grid cell and keep track of visited squares to avoid
repeated calculations. Each call to bfs will traverse through an island this way.

Time Complexity: O(mn) because we visit every grid square once
Space Complexity: O(mn) because we keep a set of visited squares

Problem Link: https://leetcode.com/problems/number-of-islands/
'''

from typing import List
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()
        
        # BFS function
        def bfs(r, c):
            visited.add((r, c))
            q = collections.deque()
            q.append((r,c))
            
            while q:
                i, j = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                # Consider all 4 non-diagonally adjacent squares
                for dr, dc in directions:
                    nr, nc = i+dr, j+dc

                    # If the square is within bounds, hasn't been visited and is "land", we add to our queue
                    if (0 <= nr and nr < rows) and (0 <= nc and nc < cols) and (nr, nc) not in visited and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        visited.add((nr, nc))
            
        # Go through all squares and bfs
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "0":
                    continue
                
                if not (r,c) in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands
