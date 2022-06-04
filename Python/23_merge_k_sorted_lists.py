'''
This file implements the solution to merge k sorted lists problem. The idea is to keep a minheap of size k to pick the minimum element and push to heap
the next values from the list that was extracted from. Since minheap does adding in O(log k) and we process N elements, this solution is O(N log k).

Time Complexity: O(N log k)
Storage Complexity: O(N + k) => N from the result building and k from the heap.

Problem Link: https://leetcode.com/problems/merge-k-sorted-lists/
'''


import heapq
from typing import List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        kHeap = []
        k = len(lists)
        result = ListNode()
        current = result
        
        for i in range(k):
            if lists[i] is not None:
                kHeap.append((lists[i].val, i))
        
        heapq.heapify(kHeap)
        
        while kHeap:
            _, idx = heapq.heappop(kHeap)
            current.next = lists[idx]
            current = current.next
            lists[idx] = lists[idx].next
            
            if lists[idx] is not None:
                heapq.heappush(kHeap, (lists[idx].val, idx))
        
        return result.next