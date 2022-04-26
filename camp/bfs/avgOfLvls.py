# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def bfs(Root):
            avgs = []
            q1, q2 = deque([]),deque([])
            q1.append(Root)
            
            while q1:
                i = num = 0
                while q1:
                    curr = q1.popleft()
                    num += curr.val
                    i +=1
                    if curr.left:
                        q2.append(curr.left)
                    if curr.right:
                        q2.append(curr.right)
                avgs.append(num/i)
                q1 = q2
                q2 = deque([])
            return avgs
        return bfs(root)
                
        
