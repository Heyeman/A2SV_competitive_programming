class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def dfs(row, col):
            visited.add((row,col))
            if board[row][col] == 'E':
                num = 0 
                for x,y in mvt:
                    nR, nC = row + x, col + y
                    if in_bound(nR, nC) and board[nR][nC] == 'M'  and (nR, nC) not in visited:
                        num += 1
                if num > 0:
                    board[row][col] = str(num)
                else:
                    board[row][col] = 'B'
                    for x,y in mvt:
                        nR, nC = row + x, col + y
                        if in_bound(nR, nC) and board[nR][nC] in 'EB' and (nR, nC) not in visited:
                            dfs(nR,nC)
                    
        
        mvt = [(0,1), (0,-1), (1,0), (-1,0),(-1,-1), (-1,1), (1,-1), (1,1)]
        in_bound = lambda x,y: 0<= x < len(board) and 0 <= y < len(board[0]) 
        visited = set()
        
        if board[click[0]][click[1]] == 'M':
                board[click[0]][click[1]] = 'X'
                return board
        dfs(click[0], click[1])
        return board
