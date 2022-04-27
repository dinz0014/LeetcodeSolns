'''
This file implements the solution to the Merge Intervals problem. The idea is pretty simple here. We first sort the intervals array according to the start points.
We can then compare adjacent intervals and merge if need be.

Time Complexity: O(N log N) since we have to sort the intervals array
Space Complexity: O(1) Auxiliary but O(N) total since the result needs to be constructed

Problem Link: https://leetcode.com/problems/merge-intervals/
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n == 1:
            return intervals
        
        # Sort according to the start point
        intervals.sort(key = lambda x: x[0])
        result = []
        currentInterval = intervals[0]
        
        # At the end of this loop currentInterval will point to last interval in result
        for i in range(1, n):
            # If intervals[i] overlaps with currentInterval, merge them and move on
            if intervals[i][0] <= currentInterval[1]:
                currentInterval = [min(currentInterval[0], intervals[i][0]), max(currentInterval[1], intervals[i][1])]
            else:
                # If they don't overlap, currentInterval is final. Add to results and move on
                result.append(currentInterval)
                currentInterval = intervals[i]
            
        result.append(currentInterval)
        return result