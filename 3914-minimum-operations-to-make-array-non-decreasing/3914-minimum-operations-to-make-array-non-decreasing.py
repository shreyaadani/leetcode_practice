class Solution:
    def minOperations(self, nums: list[int]) -> int:
        x=0
        for i in range(1,len(nums)):
            x += max(0,nums[i-1]-nums[i])


        return x 