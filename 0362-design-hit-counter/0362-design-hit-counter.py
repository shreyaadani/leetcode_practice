class HitCounter:

    def __init__(self):
        self.hits = [0]*300
        self.count = [0]*300
        

    def hit(self, timestamp: int) -> None:
        idx = timestamp % 300
        if self.hits[idx] != timestamp:
            self.hits[idx] = timestamp
            self.count[idx] = 1
        else:
            self.count[idx]+=1    
        

    def getHits(self, timestamp: int) -> int:
        totalhits = 0
        for i in range(300):
            if timestamp - self.hits[i] < 300:
                totalhits+= self.count[i]

        return totalhits        



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)