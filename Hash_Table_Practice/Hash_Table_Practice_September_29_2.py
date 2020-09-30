class HashTable:
    def __init__(self):
        self.MAX = 5
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, data):
        h = 0
        for char in data:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val) # at index of this location, add this
                found = True
                break
        if not found: # if item doesn't already exist
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        # self.arr[h] # is whole list
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]): # get list, then go through each element
            if element[0] == key: # every element[0] is a key
                del self.arr[h][index]


t = HashTable()
t["march 4"] = 120
t["march 5"] = 20
t["march 6"] = 12
t["march 7"] = 2
t["march 1"] = 20
t["march 2"] = 12
t["march 3"] = 2
print(t.arr)
del t['march 6']
print(t.arr)
print(t['march 2'])