class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        nmap = set()
        for i in range(len(nums)):
            if nums[i] in nmap:
                return True
            nmap.add(nums[i])
            if len(nmap) > k:
                nmap.remove(nums[i-k])

        return False            

        