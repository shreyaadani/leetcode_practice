class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l + r) // 2
            pieces = 1          # start with one subarray
            curr = 0
            for n in nums:
                if curr + n > mid:      # n overflows current piece
                    pieces += 1
                    curr = 0
                curr += n               # INSIDE the loop
            if pieces > k:              # too many -> limit too small -> bigger
                l = mid + 1
            else:
                r = mid
        return l