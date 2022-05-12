# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, sums):
            nonlocal res
            if root and root.left:
                dfs(root.left, sums+root.val)
            if root and root.right:
                dfs(root.right, sums+root.val)
            if root and not root.left and not root.right and sums+root.val == targetSum:
                res = True
                
        
        
        
        
        
        res = False
        dfs(root, 0)
        return res
            
        
