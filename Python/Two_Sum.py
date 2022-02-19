from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        m = {}
        
        for i in range(N):
            if target - nums[i] in m:
                return [i, m[target - nums[i]]]
            else:
                m[nums[i]] = i