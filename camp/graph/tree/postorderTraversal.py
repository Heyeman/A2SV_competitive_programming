# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def values(root):
            if not root:
                return []
            res = []
            if root.left:
                res.extend(values(root.left))
            if root.right:
                res.extend(values(root.right))
            res.append(root.val)
            return res
        return values(root)
        
