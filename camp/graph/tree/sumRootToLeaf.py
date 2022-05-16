# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def nums(root, num):
            nonlocal numbers
            if root.left:
                nums(root.left, num+str(root.val))
            if root.right:
                nums(root.right, num+str(root.val))
            if not root.right and not root.left:
                numbers += int(num+ str(root.val))
                

                
            
            
            
        numbers = 0
        nums(root, "")
        return numbers
