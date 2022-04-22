'''
This file implements the solution to Search 2D Matrix problem on leetcode. The key is to think of the matrix as a sorted list and perform normal binary search

Time Complexity: O(log M*N)
Space Complexity: O(1)

Problem Link: https://leetcode.com/problems/search-a-2d-matrix/
'''


from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)
        l, r = 0, m*n-1
        
        while l < r:
            mid = (l+r)//2
            
            # Mapping the flattened index to row and column
            midR = mid//m
            midC = mid%m
            
            if matrix[midR][midC] < target:
                l = mid+1
            else:
                r = mid
        
        # Left pointer should now be at the target if it is in the matrix
        return matrix[l//m][l%m] == target