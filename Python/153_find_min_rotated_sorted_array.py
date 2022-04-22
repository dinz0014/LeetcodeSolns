'''
This file implements the solution to the problem Find Minimum in Rotated Sorted Array. The trick here is to binary search and consider three cases.
If nums[l] <= nums[r], nums[l] is the minimum. The reason for this is that we start with l=0 and r=n-1 and if an array is rotated the first element must be 
bigger than the last element. So, if that was not the case, we must have the minimum somewhere between l and r. We calculate the mid point m. Now, if nums[m] >= nums[l], 
the minimum must be somewhere in nums[m+1:r]. Otherwise, we must have nums[m] <= nums[r]. In this case, the subarray nums[l:m+1] has the minimum.

Time Complexity: O(log N)
Space Complexity: O(1)

Problem Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
'''

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        
        while l <= r:
            # If number at l is less than number at r number at l must be the minimum
            if nums[l] <= nums[r]:
                return nums[l]
            
            m = (l+r)//2
            
            # Cut down appropriate half based on the comparisons of nums[l], nums[m] and nums[r]
            if nums[l] <= nums[m]:
                l = m+1
            elif nums[m] <= nums[r]:
                r = m