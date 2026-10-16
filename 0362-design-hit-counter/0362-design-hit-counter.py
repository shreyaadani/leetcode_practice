class HitCounter:

    def __init__(self):
        self.hits = []
        

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        l , r = 0, len(self.hits)-1
        target = timestamp - 300

        while l<=r:
            mid = (l+r) // 2

            if self.hits[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1

        return len(self.hits) - l            
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)