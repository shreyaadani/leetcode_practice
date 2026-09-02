class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minp = float("inf")

        for i in range(len(prices)):
            if prices[i] < minp:
                minp = prices[i]
            elif prices[i] - minp > res:
                res = prices[i] - minp

        return res            

