class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        original = image[sr][sc]

        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or image[i][j] != original:
                return
            image[i][j]= color
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        if original != color:
             dfs(sr,sc)
        return image        