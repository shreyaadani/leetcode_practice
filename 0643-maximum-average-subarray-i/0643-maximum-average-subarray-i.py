class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
          total = sum(nums[0:k])
          max_total = total

          for i in range(0, len(nums) - k):
                total -= nums[i]
                total += nums[i + k]
                max_total = max(max_total, total)

          return max_total / k

