class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(row,col, onBorder):
            nonlocal count
            visited.add((row,col))
            for x,y in dxn:
                newR, newC = row + x, col + y
                if in_bound(newR,newC) and (newR,newC) not in visited and grid[newR][newC] == 1:
                    if onBorder:
                        dfs(newR, newC, True)
                    else:
                        dfs(newR, newC, False)
                        
            if onBorder:
                grid[row][col] = 0
            else:
                count +=1
                        
                        

        
        
        
        
        visited = set()
        count = 0
        in_bound = lambda x, y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        on_border = lambda x,y: 0 == x or x == len(grid)-1 or 0 == y or y == len(grid[0])-1
        dxn = [(0,1), (0,-1), (1,0), (-1,0)]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and on_border(i,j) and (i,j) not in visited:
                    # print("true")
                    dfs(i,j, True)
 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and in_bound(i,j) and (i,j) not in visited:
                    dfs(i,j, False)
        return count
                    
                     
                    
                    
                    
                    
                    
                    
                    
        
        
