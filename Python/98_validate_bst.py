'''
This file validates a BST implemented via a TreeNode class. It works by verifying that each node has a value that lies in between the maximum value in the left
subtree and the minimum in the right subtree.

Time Complexity: O(V) cus of DFS
Space Complexity: O(V) due to stack use in recursion
Problem link: https://leetcode.com/problems/validate-binary-search-tree/
'''

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        INF = float("inf")
        
        def dfs(node, mn, mx):
            if node is None:
                return True
            
            if node.val <= mn or node.val >= mx:
                return False
            
            left, right = False, False
            left = dfs(node.left, mn , node.val)
            right = dfs(node.right, node.val, mx)
            
            return left and right
        
        return dfs(root, -INF, INF)