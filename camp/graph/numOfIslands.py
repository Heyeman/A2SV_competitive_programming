class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            visited.add((row,col))
            for x,y  in mvt:
                nR, nC = x+row, y + col
                if in_bound(nR, nC) and grid[nR][nC] == "1" and (nR, nC) not in visited:
                    dfs(nR, nC)
                    
                    
        
        
        
        
        visited = set()
        mvt = [(1,0), (-1,0), (0,1), (0,-1)]
        in_bound = lambda x,y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    islands +=1
        return islands
