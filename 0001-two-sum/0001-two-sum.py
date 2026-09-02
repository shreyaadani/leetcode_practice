class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nmap:
                return [i, nmap[diff]]
            else:
                nmap[nums[i]] = i  
                
        