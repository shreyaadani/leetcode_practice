class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.dic[val] = len(self.list)
        self.list.append(val)
        return True    
        

    def remove(self, val: int) -> bool:
        if val in self.dic:
            last_element, idx = self.list[-1], self.dic[val]
            self.list[idx], self.dic[last_element] = last_element, idx
            # delete the last element
            self.list.pop()
            del self.dic[val]
            return True
        return False
        

    def getRandom(self) -> int:
        return choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()