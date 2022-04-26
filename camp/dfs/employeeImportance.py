"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def dfs(num):
            val = adj[num][0]
            for i in adj[num][1]:
                val += dfs(i)
                
            return val
        
        
        
    
        
        adj = dict()
        for i in employees:
            adj[i.id] = (i.importance,i.subordinates)
        return dfs(id)
        
