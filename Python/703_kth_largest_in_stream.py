'''
This file implements the solution to finding the Kth largest element in a stream. The idea is to have a heap that keeps only the k largest elements.
If at any point during the addition of an element, the length of the heap exceeds k, we pop the minimum element.

Time Complexity: init is O(N log N) where N is the size of nums. Add is O(Log N) since pushing into a max/min heap requires the shuffling of elements to keep heap invariant
Space Complexity: O(k) since the heap is at most k elements.

Problem Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/
'''

from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Sort the list and keep only the largest k elements in heap
        self.pq = sorted(nums, reverse = True)[:k]
        heapq.heapify(self.pq)
        self.k = k

    def add(self, val: int) -> int:
        # Push to heap, check if length exceeds k and pop
        heapq.heappush(self.pq, val)
        
        if len(self.pq) > self.k:
            heapq.heappop(self.pq)
        
        return self.pq[0]
