class HashTable:
    def __init__(self):
        self.MAX = 4
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, char):
        h = 0
        for letter in char:
            h += ord(letter)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        isfound = False
        for index, elements in enumerate(self.arr[h]):
            if elements[0] == key:
                self.arr[h][index] = (key, value)
                isfound = True
        if isfound == False:
            self.arr[h].append((key, value))

    def __getitem__(self, item):
        h = self.get_hash(item)
        for elements in self.arr[h]:
            if elements[0] == item:
                return elements[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, elements in enumerate(self.arr[h]):
            if elements[0] == key:
                del self.arr[h][index]

if __name__ == '__main__':
    h = HashTable()
    h["As"] = 82
    h["Hia"] = 18
    h["Qai"] = 7
    h["Ss"] = 2
    h["Aa"] = 1
    h["Xi"] = 7
    print(h.arr)
    print(h["Xi"])
    del h["Xi"]
    print(h.arr)