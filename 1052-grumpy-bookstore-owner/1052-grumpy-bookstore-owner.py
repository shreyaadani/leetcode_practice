class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
       satisfied, unsatisfied, trick = 0,0,0
       
       for i, cus in enumerate(customers):
        if not grumpy[i]:
            satisfied += cus

        else:
            unsatisfied += cus
            
            
        if i>= minutes:
         unsatisfied -= customers[i-minutes]*grumpy[i-minutes]

        trick = max(trick,unsatisfied)
       return satisfied + trick  




