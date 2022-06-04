'''
This file implements the solution to House Robber II. Same as the House Robber problem but now the houses are in a circle. The idea is that we can't steal from both
first and last house. So, we run simple rob house on two lists nums[1:end] and nums[0: end-1] then pick whichever one is better.

Time Complexity: O(N) => We loop over N-1 items twice.
Space Complexity: O(1)

Problem Link: https://leetcode.com/problems/house-robber-ii/submissions/
'''

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def robSimple(i, j) -> int:
            if i == j:
                return nums[i]

            prevPrev, prev = nums[i], max(nums[i], nums[i+1])
            
            for k in range(i+2, j+1):
                curr = max(prevPrev + nums[k], prev)
                prevPrev = prev
                prev = curr

            return prev
        
        a1 = robSimple(1, len(nums)-1)
        a2 = robSimple(0, len(nums)-2)
        
        return max(a1, a2)