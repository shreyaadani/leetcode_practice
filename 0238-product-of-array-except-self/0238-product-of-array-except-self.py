class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        l,r, res = [0]*length , [0]*length, [0]*length
        l[0]=1
        for i in range(1,length):
            l[i] = nums[i-1]*l[i-1]

        r[length-1] = 1
        for i in reversed(range(length-1)):
            r[i] = nums[i+1]*r[i+1] 

        for i in range(length):
            res[i] = l[i]*r[i]

        return res          


        