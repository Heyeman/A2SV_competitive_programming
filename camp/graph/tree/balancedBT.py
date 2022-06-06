# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True
        def heightDiff(node):
            if not node:
                return 0
            
            left = heightDiff(node.left)
            right = heightDiff(node.right)
            if abs(left - right) > 1:
                self.isBalanced = False
            
            return max(left, right) + 1
        heightDiff(root)
        return self.isBalanced
        
        
