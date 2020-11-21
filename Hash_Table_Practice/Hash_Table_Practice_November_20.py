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
                break
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

if __name__ == "__main__":
    h = HashTable()
    h["a"] = 1
    h["ab"] = 12
    h["abc"] = 123
    h["abcd"] = 1234
    h["abcde"] = 12345
    h["abcdef"] = 123456
    h["abcdefg"] = 1234567
    print(h["ab"])
    print(h.arr)
    del h["ab"]
    print(h.arr)