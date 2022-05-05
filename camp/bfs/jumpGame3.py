class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def bfs(ind):
            q = deque([ind])
            visited.add(ind)
            while q:
                curr = q.popleft()
                x = y= 0
                if arr[curr] == 0:
                    return True
                x = curr - arr[curr]
                y = curr + arr[curr]
                if 0<= x < len(arr) and x not in visited:
                    q.append(x)
                    visited.add(x)
                if 0<= y < len(arr) and y not in visited:
                    q.append(y)
                    visited.add(y)
                                
                  
             
            
            
            
            
           
        jump = False
        visited = set()
        jump = bfs(start)
        return jump
        
            
            
        
        
