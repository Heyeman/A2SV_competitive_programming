# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def traverse(root, fatherEven, grandEven):
            if not root:
                return 0
            if grandEven:
                nonlocal nums
                nums += root.val
            isEven = root.val % 2 == 0
            if root.left:
                traverse(root.left, isEven, fatherEven)
            if root.right:
                traverse(root.right, isEven, fatherEven)
            
    
        nums = 0
        traverse(root, False, False)
        return  nums
        
