class MyHashSet:

    def __init__(self):
        self.dictt = {}
        self.cnt=0

    def add(self, key: int) -> None:
         if key not in self.dictt.values():
            self.dictt[self.cnt] = key
            self.cnt += 1

    def remove(self, key: int) -> None:
        for index, value in self.dictt.items():
            if value == key:
                del self.dictt[index]
                return
            

    def contains(self, key: int) -> bool:
         return key in self.dictt.values()
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)