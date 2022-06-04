'''
This file implements the solution to same binary tree problem. The idea is simple, just check that each node and its children are equal recursively.

Time Complexity: O(min(N, M)) because it visits nodes of both trees simultaneously and returns false if they don't match at any point
Storage Complexity: O(min(N, M)) because of recursive stack

Problem Link: https://leetcode.com/problems/same-tree/
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False