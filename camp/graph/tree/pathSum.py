# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, num):
            if not node:
                return False
            left = right = False
            curr = num + node.val
            if node.left:
                left = dfs(node.left, curr)
            if node.right:
                right = dfs(node.right, curr)
            if not node.left and not node.right:
                return targetSum == curr
            return left or right
        return dfs(root, 0)
