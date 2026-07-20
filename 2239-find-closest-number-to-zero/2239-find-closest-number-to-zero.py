class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        solmap = [+inf,+inf] #duplicate distance

        for i in range(len(nums)):
            dis = abs(0-nums[i])
            if dis == solmap[0]:
                solmap[1] = max(solmap[1],nums[i])
            else:
                if dis < solmap[0]:
                    solmap[0] = dis
                    solmap[1]= nums[i]


        return solmap[1]            



        