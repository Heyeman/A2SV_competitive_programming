# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.res = False
        def levelOrder(node, lvlSum):
            if not node:
                return 0
            curr = lvlSum + node.val
            if node.left:
                levelOrder(node.left, curr)
            if node.right:
                levelOrder(node.right, curr)
            if not node.left and not node.right and not self.res:
                self.res = curr == targetSum
        levelOrder(root, 0)
        return self.res
                
