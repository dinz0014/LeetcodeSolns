'''
This file implements the solution to the House Robber Problem. We can use a 1D dp approach. The subproblems are 
dp[i] = the max cost that can be stolen from nums[0:i+1]. 
The optimal solution is dp[i] = max(dp[i-2] + nums[i], dp[i-1]). Note that we only need the last 2 values ever. So,
the way we reduce storage complexity is by only keeping track of the last 2 values in dp array.
'''

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        prevPrev, prev = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            curr = max(prevPrev + nums[i], prev)
            prevPrev = prev
            prev = curr
            
            
        return prev