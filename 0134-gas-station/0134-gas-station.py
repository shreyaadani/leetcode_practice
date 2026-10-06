class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        totalgain = 0
        currgain = 0
        res = 0

        for i in range(len(gas)):
            totalgain += gas[i] - cost[i]
            currgain += gas[i] - cost[i]

            if currgain < 0:
                currgain = 0
                res = i+1

        return res if totalgain >= 0 else -1                