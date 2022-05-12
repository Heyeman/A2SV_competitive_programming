# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            q = deque([root])
            res = 0
            while q:
                res += 1 
                for i in range(len(q)):
                    curr = q.popleft()
                    if not curr.left and not curr.right:
                        return res
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                
            return res
        result = dfs(root)
        return result
        
