'''
This file implements the solution to balanced binary tree problem. The idea is to recurse and find heights of left and right subtree at each node
and return early if they differ by more than 1.

Time Complexity: O(N) visits every node once
Storage Complexity: O(N)

Problem Link: https://leetcode.com/problems/balanced-binary-tree/
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        if abs(self.calcTreeHeight(root.left, 0) - self.calcTreeHeight(root.right, 0)) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def calcTreeHeight(self, node: TreeNode, currDepth: int) -> int:
        if node is None:
            return currDepth
        
        return max(self.calcTreeHeight(node.left, currDepth), self.calcTreeHeight(node.right, currDepth)) + 1