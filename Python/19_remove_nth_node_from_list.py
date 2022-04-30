'''
This file implements the solution to Removing the Nth node from the end of a linked list. The trick here is to have two pointers "f" and "l".
l initially will be exactly n nodes from the start. Then, we move f and l together until l has no next node. This way, f points to the node
that must be removed from the linked list.

Time Complexity: O(N) as we remove and return in one pass
Storage Complexity: O(1)
'''
from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        f = head
        l = head
        prev = None
        
        if n == 1 and f.next is None:
            return None
        
        for i in range(1, n):
            l = l.next
        
        while l.next is not None:
            prev = f
            l = l.next
            f = f.next
            print(prev.val, f.val, l.val)
        
        if prev is None:
            return head.next
        
        if f is not None:
            prev.next = f.next 
        else:
            prev.next = None
            
        return head