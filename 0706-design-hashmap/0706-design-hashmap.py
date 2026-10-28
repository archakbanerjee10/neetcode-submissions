class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.hashmap)):
            if self.hashmap[i][0] == key:
                self.hashmap[i][1] = value
                return
        # If the key wasn't found in the loop, append it as a new pair
        self.hashmap.append([key, value])

    def get(self, key: int) -> int:
        for i in range(len(self.hashmap)):
            if self.hashmap[i][0] == key:
                return self.hashmap[i][1]
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.hashmap)):
            if self.hashmap[i][0] == key:
                self.hashmap.pop(i)
                return