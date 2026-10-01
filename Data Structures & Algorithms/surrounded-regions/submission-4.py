class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board),len(board[0])
        def fill(i,j):
            
            if i < 0 or i >= m or j < 0 or j>=n:
                return 
            if board[i][j] != 'O':
                return 
            
            board[i][j] = '?'
            dirs = [(0,1),(1,0),(-1,0),(0,-1)]
            for dx,dy in dirs:
                fill(i+dy,j+dx)
            return
        
        for i in range(m):
            fill(i,0)
            fill(i,n-1)
        for j in range(n):
            fill(0,j)
            fill(m-1,j)   
        for i in range(m):
            for j in range(n):
                if board[i][j] == '?':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'