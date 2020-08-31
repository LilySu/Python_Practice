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
        for index, value in enumerate(self.arr[h]):
            if len(value) == 2 and value[0] == key:
                self.arr[h][index] = (key, value)
                isfound = True
                break
        if isfound == False:
            self.arr[h].append((key, value))

    def __getitem__(self, item):
        h = self.get_hash(item)
        for value in self.arr[h]:
            if value[0] == item:
                return value[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, value in enumerate(self.arr[h]):
            if value[0] == key:
                del self.arr[h][index]

if __name__ == '__main__':
    t = HashTable()
    t['March'] = 120
    t['Parch'] = 120
    t['Starch'] = 120
    t['Arch'] = 120
    t['March'] = 120
    t['Parch'] = 120
    t['Starch'] = 120
    t['Arch'] = 120
    del t['March']
    print(t['Arch'])
    print(t.arr)
