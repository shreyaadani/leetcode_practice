class TimeMap:

    def __init__(self):
        self.map = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.map:
            self.map[key] = []

        self.map[key].append([timestamp,value])

        

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ""
        if timestamp < self.map[key][0][0]:
            return ""

        l = 0
        r = len(self.map[key])

        while l < r:
            mid = (l+r) // 2
            if self.map[key][mid][0] <= timestamp:
                l = mid + 1   
            else:
                r = mid 


        return "" if r == 0 else self.map[key][r-1][1]                 
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)