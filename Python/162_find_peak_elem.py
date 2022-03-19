'''
This file contains the solution to leetcode problem Find Peak Element. We are supposed to find and return the index of an element in a list such that the element is
greater than its two neighbours.

Due to the required O(log(n)) complexity, we implement a modified binary search algorithm that kind of picks which half to search each iteration based on the fact that
at least one of the halves will have our answer. So we pick a half that is forced to kind of do a "stationary point".

Leetcode Link: https://leetcode.com/problems/find-peak-element/
'''

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        
        # Base cases
        if n == 1:
            return 0
        
        # If there are two elements return the index of bigger one
        if n == 2:
            return 0 if nums[0] > nums[1] else 1
        
        # A modified binary search 
        while l <= r:
            m = (l+r)//2
            
            # If number at m is bigger than neighbours we immediately return
            if (m == 0 or nums[m] > nums[m-1]) and (m == n-1 or nums[m] > nums[m+1]):
                return m
            
            # If the right most value is bigger than middle, we are guaranteed to find a peak in the right half
            if (nums[r] >= nums[m]):
                l = m+1
            # If the left most value is bigger than middle, we are guaranteed to find a peak in the left half
            elif nums[l] >= nums[m]:
                r = m-1
            else:
                # Here is the tricky case. When both left and right most values are less than middle, we have to shift to the half with the bigger neighbour
                # This is because we know that half must descend somewhere, and the only way to descend is to "turn back" causing a peak element to occur
                if (nums[m+1] > nums[m]):
                    l = m+1
                else:
                    r = m-1