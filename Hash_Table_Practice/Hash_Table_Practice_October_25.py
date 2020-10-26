class HashTable:
    def __init__(self):
        self.MAX = 4
        self.arr = [[] for i in range(self.MAX)]

    def gethash(self, item):
        h = 0
        for char in item:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.gethash(key)
        isfound = False
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                # insert new tuple in the same location since
                # tuples are immutable
                self.arr[h][index] = (key, value)
                isfound = True
        if isfound == False:
            self.arr[h].append((key, value))

    def __getitem__(self, item):
        h = self.gethash(item)
        for element in enumerate(self.arr[h]):
            if element[0] == item:
                return element[1]
            # by default returns none if doesn't return a value

    def __delitem__(self, key):
        h = self.gethash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]



class HashTable:
    def __init__(self):
        self.MAX = 4
        self.arr = [[] for i in range(self.MAX)]

    def gethash(self, item):
        h = 0
        for char in item:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.gethash(key)
        isfound = False
        for index, element in self.arr[h]:
            if element[0] == key:
                self.arr[h][index] = (key, value)
                isfound = True
                break
        if isfound == None:
            self.arr[h].append((key, value))

    def __getitem__(self, item):
        h = self.gethash(item)
        for element in self.arr[h]:
            if element[0] == item:
                return element[1]

    def __delitem__(self, key):
        h = self.gethash(key)
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