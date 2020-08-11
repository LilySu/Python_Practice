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
            if len(element[0]) == 2 and element[0] == key: # handles if the key already exists
                isfound = True
                self.arr[h][index] = (key, value) # modify key value pair
                break
        if isfound == False:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1] # would return none if it doesn't return anything

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

# probing means finding a slot to store key value pair
if __name__ == '__main__':
    h = HashTable()
    h['mon'] = 12
    h['go'] = 23
    h['ro'] = 34
    h['qon'] = 12
    h['wo'] = 23
    h['ho'] = 34
    h['xon'] = 12
    h['vo'] = 23
    h['zo'] = 34
    del h['zo']
    # print(h['zo'])
    print(h.arr)



def __setitem__(self, key, value):
    h = self.get_hash(key)
    found = False
    for index, element in enumerate(self.arr[h]):
        if element[0] == 2 and element[0] == key:
            self.arr[h][index] = (key, value)
            found = True
            break
    if found == False:
        self.arr[h].append((key, value))

def __getitem__(self, key):
    h = self.get_hash(key)
    for element in enumerate(self.arr[h]):
        if element[0] == key:
            return element[1]

def __delitem__(self, key):
    h = self.get_hash(key)
    for index, element in enumerate(self.arr[h]):
        if element[0] == key:
            del self.arr[h][index]