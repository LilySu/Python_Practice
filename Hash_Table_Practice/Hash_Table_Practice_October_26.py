class HashTable:
    def __init__(self):
        self.MAX = 4
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, item):
        h = 0
        for char in item:
            h += ord(char)
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

    def __getitem__(self, item):
        h = self.get_hash(item)
        for element in self.arr[h]:
            if element[0] == item:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            element[0] == key
            del self.arr[h][index]


if __name__ == '__main__':
    h = HashTable()
    h["Mon"] = 1
    h["Ron"] = 3
    h["Ewon"] = 43
    h["Mn"] = 1
    h["Rn"] = 3
    h["En"] = 43
    # print(h["Ron"])
    del h["Ewon"]
    print(h.arr)