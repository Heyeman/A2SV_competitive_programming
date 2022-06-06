# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swapper(node):
            if not node:
                return
            temp = node.left
            node.left = node.right
            node.right = temp
            swapper(node.left)
            swapper(node.right)
        swapper(root)
        return root
        
