class HashTable:
    def __init__(self):
        self.MAX = 4
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, data):
        h = 0
        for i in data:
            h += ord(i)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        isfound = False
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][index] = (key, value)
                isfound = True
                break
        if isfound == False:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, elements in enumerate(self.arr[h]):
            if elements[0] == key:
                del self.arr[h][index]

if __name__ == '__main__':
    h = HashTable()
    h["mon"] = 19
    h["bew"] = 23
    h["ui"] = 123
    print(h.arr)
    print(h["ui"])
    del h["ui"]
    print(h.arr)