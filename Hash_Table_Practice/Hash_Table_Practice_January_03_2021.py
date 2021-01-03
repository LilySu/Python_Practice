class HashTable:
    def __init__(self):
        self.MAX = 4
        self.arr = [[] for i in range(self.MAX)]

    def hash(self, item_to_hash):
        h = 0
        for item in item_to_hash:
            h += ord(item)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.hash(key)
        isfound = False
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][index] = (key, value)
                isfound = True
                break
        if isfound == False:
            self.arr[h].append((key, value))

    def __getitem__(self, item):
        h = self.hash(item)
        for element in self.arr[h]:
            if element[0] == item:
                return element[1]

    def __delitem__(self, key):
        h = self.hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

if __name__ == '__main__':
    h = HashTable()
    h["sloth"] = 22
    h["rabbit"] = 4
    h["squirrel"] = 33
    h["penguin"] = 9
    h["dog"] = 5
    h["starfish"] = 7

    print(h.arr)
    print( "sloth is number: ", h["sloth"])
    del h["sloth"]
    print(h.arr)