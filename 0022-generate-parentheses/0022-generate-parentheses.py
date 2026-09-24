class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def dfs(s,left,right):
            if len(s) == 2*n:
                res.append(s)

            if left > 0:
                dfs(s+'(',left-1,right)

            if right > 0 and right>left:
                dfs(s+')',left,right-1)

        dfs("",n,n)

        return res            

