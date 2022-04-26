class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(row,col):
            visited.add((row,col))
            
            for x,y in dxn:
                newRow, newCol = row+x, col+ y
                if in_bound(newRow, newCol) and image[row][col] == image[newRow][newCol] and (newRow, newCol) not in visited:
                    dfs(newRow, newCol)
            image[row][col] = newColor

        
        
        
        visited = set()
        dxn = [(1,0), (-1,0), (0,1), (0,-1)]
        in_bound = lambda x, y: 0 <= x < len(image) and 0<= y < len(image[0])
        dfs(sr, sc)
        return image
