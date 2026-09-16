class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        directions = [[0,-1],[0,1],[1,0],[-1,0]]
        row = len(grid)
        col = len(grid[0])
        time = 0
        fresh = 0


        queue = deque()

        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    queue.append((i,j))
                if grid[i][j]==1:
                     fresh += 1


        while queue:
            qlen= len(queue)
            rotten = False
            for q in range(qlen):
                r,c = queue.popleft()
                for dr,dc in directions:
                    nr,nc = dr+r, dc+c
                    if (nr in range(row) and nc in range(col) and grid[nr][nc]==1):
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        fresh -= 1
                        rotten = True
            if rotten:
                time+=1

       

        return time if fresh==0 else -1


        






        