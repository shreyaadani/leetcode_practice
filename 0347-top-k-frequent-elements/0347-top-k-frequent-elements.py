class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       if k == len(nums):
        return nums
       heap = []
       count = Counter(nums)

       for key in count.keys():
        heapq.heappush(heap,(count[key],key))
        if len(heap) > k:
            heapq.heappop(heap)

       return [i[1] for i in heap]   


        