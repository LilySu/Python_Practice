class HashTable:
    def __init__(self):
        self.MAX = 4
        self.arr = [[] for i in range(self.MAX)]

    def hash(self, data):
        h = 0
        for i in data:
            h += ord(data)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.hash(key)
        