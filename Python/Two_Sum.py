from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        m = {} # Maps numbers in nums to the corresponding index
        
        for i in range(N):
            # If the required number is in the map, we have seen it before so we have found the answer
            if target - nums[i] in m:
                return [i, m[target - nums[i]]]
            else:
                # Otherwise, add the current number and index to map
                m[nums[i]] = i