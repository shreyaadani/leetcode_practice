class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       buckets = [[] for _ in range(len(nums)+1)] #independant list for every index
       count = Counter(nums)
       for num,freq in count.items():
        buckets[freq].append(num)

       res = []
       for i in range(len(buckets)-1,0,-1):
        for num in buckets[i]:
            res.append(num)
            if len(res) == k:
                return res


        