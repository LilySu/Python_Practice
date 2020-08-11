class HashTable:
    def __init__(self):
        self.MAX = 4
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, data):
        h = 0
        for item in data:
            h += ord(item)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for index, element in self.arr[h]:
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, value)
                found = True
                break
        if found == False:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]


    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in self.arr[h]:
            if element[0] == key:
                del self.arr[h][index]



if __name__ == '__main__':
    a = HashTable()
    print(a.get_hash("Mon"))
    pass
