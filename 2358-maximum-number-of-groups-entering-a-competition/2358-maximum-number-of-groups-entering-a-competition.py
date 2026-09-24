class Solution:
    def maximumGroups(self, grades: list[int]) -> int:
        n = len(grades)
        k=0
        while n>=k+1:
            k = k+1
            n= n-k

        return k
        