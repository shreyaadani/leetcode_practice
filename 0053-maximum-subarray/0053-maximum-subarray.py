class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        currentsum = nums[0]

        for num in nums[1:]:
          currentsum = max(currentsum+num, num)
          maxsum = max(currentsum , maxsum)


        return maxsum  
        