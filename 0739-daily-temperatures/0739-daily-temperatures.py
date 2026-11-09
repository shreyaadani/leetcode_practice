class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        ans = [0]*n

        stack = []

        for curday, curtemp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curtemp:
                prevday = stack.pop()
                ans[prevday] = curday - prevday 
            stack.append(curday)


        return ans        
        