'''
This file implements the solution to jump game problem. The key idea is that we loop for i from end to start and find the first i that is able to reach the current
index we are at. Then, the current index is updated to be i. This process guarantees a solution.

Time Complexity: O(N)
Storage Complexity: O(1)

Problem Link: https://leetcode.com/problems/jump-game/
'''

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current = len(nums) - 1
        
        if not current: return True
        
        for i in range(current-1, -1, -1):
            if nums[i] + i >= current:
                current = i    
        
        return True if current == 0 else False