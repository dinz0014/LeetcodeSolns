'''
This file implements the solution to the remove adjacent duplicates II problem. The idea is to keep track of consecutive character counts in a stack and pop
whenever the count of the top most character is k. Every element in the stack is of the form [character, count] where character is a specific character
that is present in the string and the variable count represents the count of characters occurring consecutively until the current position in the string.
Elements are structured as lists to increment count in-place.

Time Complexity: O(N)
Space Complexity: O(N)

Problem Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
'''

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        # Iterate through all the characters
        for c in s:

            # If stack is empty, add element and continue
            if not stack:
                stack.append([c, 1])
                continue
            
            # Check if last seen character is same as current one. If they aren't, add to stack and continue
            topC, _ = stack[-1]
            if topC != c:
                stack.append([c, 1])
                continue
            
            # Otehrwise, increment count and pop when count == k
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
                
        # Now, the remaining elements in stack represent the string 
        return "".join([c*k for c, k in stack])