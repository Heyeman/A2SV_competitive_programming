# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        totalTilt = 0
        def tilter(node):
            nonlocal totalTilt
            if not node:
                return 0
            left = tilter(node.left)
            right = tilter(node.right)
            totalTilt += abs(left - right)
            return left + right + node.val
        tilter(root)
        return totalTilt
            
            
        
