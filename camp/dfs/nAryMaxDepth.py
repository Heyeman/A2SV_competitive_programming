"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(root, depth):
            if not root:
                depths.add(0)
                return
            for i in range(len(root.children)):
                dfs(root.children[i], depth+1)
            
            if not root.children:
                depths.add(depth + 1)
            
        
        
        depths = set()
        dfs(root, 0)
        return max(depths)
