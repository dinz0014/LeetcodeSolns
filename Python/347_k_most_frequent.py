'''
This file implements the solution to the top k most frequent elements problem from Leetcode. The idea is to count the frequencies, and sort them using bucket sort.
A different sort would result in O(N log(N)) time complexity. But bucket sort can achieve O(N).

Time Complexity: O(N) because the last loop is worst case O(N)
Storage Complexity: O(N) for the buckets and Counter object

Problem Link: https://leetcode.com/problems/top-k-frequent-elements/
'''

from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums) # Get frequencies
        n = len(nums)
        buckets = [[] for _ in range(n)] # buckets[i] is a list of elements in "nums" that have frequency i+1
        
        # Update buckets 
        for x in c:
            buckets[c[x] - 1].append(x)
        
        # Get k elements from top buckets
        results = []
        cnt = 0
        for i in range(n-1, -1, -1):
            for n in buckets[i]:
                results.append(n)
                cnt += 1
                if cnt == k:
                    return results