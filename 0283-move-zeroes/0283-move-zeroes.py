class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i+=1
        
        if i < len(nums):
            for num in range(i,len(nums)):
                nums[num] = 0
                

        