'''
This file implements the solution to finding the diameter of a binary tree problem. The idea is simple. Either the longest path runs through current node from left child
to right child, or it passes from left/right child to the parent. Update a global variable that keeps track of the maximumPath length.

Time Complexity: O(N) because dfs for tree
Space Complexity: O(N) for recursion stack

Problem link: https://leetcode.com/problems/diameter-of-binary-tree/
'''
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        # Stores maximum length path
        self.maxPath = -1
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # If at a leaf, no paths so return 0
            if node is None:
                return 0
            
            leftDepth = dfs(node.left) # Go left
            rightDepth = dfs(node.right) # Go right

            # Update maximum path length
            self.maxPath = max(self.maxPath, leftDepth + rightDepth)
            
            # Return if at root
            if node == root:
                return self.maxPath
            
            # If not at root, pass up the longest path to parent
            return max(leftDepth, rightDepth) + 1
        
        return dfs(root)