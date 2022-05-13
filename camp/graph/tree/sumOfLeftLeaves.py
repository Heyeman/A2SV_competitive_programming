# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def leaveSum(root, isLeft = False):
            if not root:
                return 0
            left = right = 0
            if root.left:
                left += leaveSum(root.left, True)
            if root.right:
                right += leaveSum(root.right)
            if isLeft and not root.left and not root.right:
                left += root.val
            return left + right
        return leaveSum(root)
        
