class MyHashMap:

    def __init__(self):
        self.dictt={}

    def put(self, key: int, value: int) -> None:
        self.dictt[key] = value

    def get(self, key: int) -> int:
        if key in self.dictt:
            return self.dictt[key]
        return -1

    def remove(self, key: int) -> None:
         if key in self.dictt:
            del self.dictt[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)