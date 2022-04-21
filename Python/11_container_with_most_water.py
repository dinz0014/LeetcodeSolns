'''
This file implements the solution to the Container with Most Water problem from Leetcode. The code below implements a greedy solution in which we use two pointers
that converge in the middle. The pointer that gets updated is the pointer which has a lower height.

Time Complexity: O(N)
Storage Complexity: O(1)

Problem Link: https://leetcode.com/problems/container-with-most-water/
'''

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, area = 0, len(height) - 1, 0
        
        # Greedily update left and right pointer
        while l < r:
            min_height=min(height[l], height[r])
            
            # Update max area
            area = max(area, (r - l) * min_height)
            
            # This is a slight optimisation than just decrementing/incrementing by 1 
            # Look for the next best height iteratively and only calculate area when necessary
            if height[l] < height[r]:
                l+=1
                while height[l]<min_height:
                    l+=1
            else:
                r-=1
                while height[r]<min_height:
                    r-=1
                    
        return area