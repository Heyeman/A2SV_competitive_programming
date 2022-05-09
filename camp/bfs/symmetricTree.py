# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def bfs(root):
            q = deque([root])
            visited.add(root)
            while q:
                l = len(q)
                for i in range(l):
                    if (type(q[i]) != type(q[l - i-1])) or ((q[i] and q[l-i-1]) and q[i].val != q[l - i-1].val):
                        return False
    
                for i in range(l):  
                    curr = q.popleft()
                    if curr:
                        q.append(curr.left)
                        q.append(curr.right)
                    visited.add(curr)
            return True
                 
                
        visited = set()
        return bfs(root)
     
        
