class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            visited.add((row,col))
            a = 1
            for x,y  in mvt:
                nR, nC = x+row, y + col
                if in_bound(nR, nC) and grid[nR][nC] and (nR, nC) not in visited:
                    dfs(nR, nC)
            areas.append(a)
                    
                    
        
        
        
        
        visited = set()
        mvt = [(1,0), (-1,0), (0,1), (0,-1)]
        in_bound = lambda x,y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        areas = []
        maxA = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] and (i,j) not in visited:
                    dfs(i,j)
                    maxA = max(maxA, len(areas))
                    areas = []
                    
        return maxA
