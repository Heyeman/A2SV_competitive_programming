# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(node):
            q = deque([node])
            # print("q", q)
            vals = []
            while q:
                curr = q.popleft()
                if curr:
                    vals.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
                else:
                    vals.append(None)

            return vals
                
                
            

            
            
        
       
        l1, l2 = [], []
        l1  = bfs(p)
        l2 = bfs(q)
        return l1 == l2
        
