class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(row, col):
            visited.add((row,col))
            
            for x,y in mvt:
                nR, nC = row+x, col + y
                if in_bound(nR,nC) and board[nR][nC] == "O" and (nR, nC) not in visited:
                    dfs(nR, nC)
                    
        
        
        mvt = [(0,1), (0,-1), (1,0), (-1,0)]
        in_bound= lambda x, y: 0 <= x < len(board) and 0 <= y <len(board[0])
        on_border = lambda x, y: 0 == x or x == len(board)-1 or 0 == y or y == len(board[0])-1
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in visited and board[i][j]=="O" and on_border(i,j):
                    dfs(i,j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i,j) not in visited:
                    board[i][j] = "X"
                    
                
        
        
