class HashTable:
    def __init__(self):
        self.MAX = 4
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, data):
        h = 0
        for letter in data:
            h += ord(letter)
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
            if element[0] == key:
                del self.arr[h][index]

if __name__ == '__main__':
    h = HashTable()
    h["Asd"] = 23
    h["ho"] = 12
    h["d"] = 23
    h["o"] = 12
    h["A"] = 23
    h["r"] = 12
    h["s"] = 23
    h["e"] = 12
    print(h.arr)
    print(h["e"])
    del(h["e"])
    print(h.arr)
