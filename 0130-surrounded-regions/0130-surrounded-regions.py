class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        row = len(board)
        col = len(board[0])
        queue = deque()

        for i in range(row):
            for j in (0,col-1):
                if board[i][j]=='O':
                    board[i][j]='S'
                    queue.append((i,j))


        for j in range(col):
            for i in (0,row-1):
                if board[i][j]=='O':
                    board[i][j]='S' 
                    queue.append((i,j))

        while queue:
            i,j = queue.popleft()
            for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
                ni,nj = di+i,dj+j
                if 0 <= ni < row and 0 <= nj < col and board[ni][nj] == 'O':
                    board[ni][nj]='S'
                    queue.append((ni,nj))        

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j]=='S':
                    board[i][j]="O"



