'''
This file implements the solution to the problem insert interval. The concept is pretty simply, the implementation is the difficult part. The key idea here is that
we loop over all the existing intervals and compare the new interval in 3 cases.
1. If the new interval has a lesser endpoint than the start of intervals[i], the new interval needs to be put in result then and there
2. If the new interval has a greater startpoint than the end of intervals[i], intervals[i] can just be added in to the result then and there
3. Otherwise, we need to merge new interval with intervals[i].

Time Complexity: O(N)
Space Complexity: O(1) Auxiliary, but O(N) total since result array is being built

Problem Link: https://leetcode.com/problems/insert-interval/ 
'''

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        result = []
        
        for i in range(n):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        result.append(newInterval)
        return result