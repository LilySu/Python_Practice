class HashTable:
    def __init__(self):
        self.MAX = 4
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
        if found == False:
            self.arr[h].append((key, val)) # if does not exist

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

t = HashTable()
t['march 6'] = 130
t['march 7'] = 13
t['march 8'] = 30
t['march 9'] = 10
print(t.arr)
print(t['march 6'])
del t['march 6']
print(t.arr)