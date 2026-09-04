class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # n = len(nums)
        # count = Counter(nums)

        # for i in count:
        #     if count[i] > n//2:
        #         return i

       candidate = None
       count = 0
       for num in nums:
            if count == 0:
                candidate = num      # adopt a new candidate when count hits 0
            if num == candidate:
                count += 1           # vote for
            else:
                count -= 1           # vote against
       return candidate


        