class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs(queues):
            q = deque(queues)
            q2 = deque([])
            mins = 0
            while q:
                mins +=1
                while q:
                    curr = q.popleft()
                    # print("curr" ,curr)
                    for x,y in mvt:
                        nR, nC = curr[0] + x, curr[1] + y
                        if in_bound(nR,nC) and (nR, nC) not in visited and grid[nR][nC] == 1:
                            # print("if passed")
                            grid[nR][nC] = 2
                            visited.add((nR,nC))
                            q2.append((nR, nC))
                
                q = q2
                q2 = deque([])
            return mins
            
        visited = set()
        total = 0
        mvt = [(0,1), (0,-1), (1,0),(-1,0)]
        in_bound = lambda x,y: 0 <= x< len(grid) and 0 <= y <len(grid[0])
        rotten = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == 2:
                    rotten.append((i,j))
        
        total = bfs(rotten)
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                           return -1
        if not total:
            return 0
        return total-1
                
        
