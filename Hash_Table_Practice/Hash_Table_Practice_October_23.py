class HashTable:
    def __init__(self):
        self.Max = 4
        self.arr = [[] for i in range(self.Max)]

    def get_hash(self, value):
        h = 0
        for item in str(value):
            h += ord(item)
        return h % self.Max

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        isfound = False
        for index, element in self.arr[h]:
            if element[0] == key:
                self.arr[h][index] = ((key, value))
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
        for index, element in self.arr[h]:
            if element[0] == key:
                del self.arr[h][index]

if __name__ == "__main__":
    t = HashTable()
    t["mar 5"] = 120
    t["mar 1"] = 12
    t["mar 3"] = 20
    t["mar 15"] = 2
    t["mar 2"] = 1
    print(t.arr)
    print(t["mar 15"])