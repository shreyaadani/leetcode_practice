class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
       self.rows = len(board)
       self.cols = len(board[0])
       self.board = board

       for row in range(self.rows):
        for col in range(self.cols):
            if self.backtrack(row,col,word):
                return True

       return False

    def backtrack(self,row:int,col:int,suf:str):
        if len(suf) == 0:
            return True

        if(
            row < 0
            or row == self.rows
            or col < 0
            or col == self.cols
            or self.board[row][col] != suf[0]
        ): return False

        ret = False
        self.board[row][col] = '#'
        for rowoff, coloff in [(0,1),(1,0),(0,-1),(-1,0)]:
            ret = self.backtrack(row+rowoff,col+coloff,suf[1:])
            if ret:
                break

        self.board[row][col] = suf[0]
        return ret                