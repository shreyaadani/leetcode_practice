class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = Counter(nums)

        for i in count:
            if count[i] > n//2:
                return i

        