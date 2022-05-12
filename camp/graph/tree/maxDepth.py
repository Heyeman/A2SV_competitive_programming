# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            if not root:
                return 0
            res = 0
            q = deque([root])
            while q:
                res +=1
                for _ in range(len(q)):
                    curr = q.popleft()
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
            return res
        return depth(root)
        
