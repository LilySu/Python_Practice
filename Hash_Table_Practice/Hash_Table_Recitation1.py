class HashTable:
    def __init__(self):
        self.MAX = 4
        # self.arr = [None] * self.MAX
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, data):
        h = 0
        for letter in data:
            h += ord(letter)
        return h % self.MAX

    # def add(self, key, value):
    #     h = self.get_hash(key)
    #     self.arr[h] = value
    # def __setitem__(self, key, value):
    #     h = self.get_hash(key)
    #     self.arr[h] = value
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element[0]) == 2 and element[0] == key:
                self.arr[h][index] = (key, value)
                found = True
                break
        if found == False:
            self.arr[h].append((key, value))


    # def get(self, key):
    #     h = self.get_hash(key)
    #     print(self.arr[h])
    # def __getitem__(self, key):
    #     h = self.get_hash(key)
    #     print(self.arr[h])
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

if __name__ == '__main__':
    h = HashTable()
    # h.add("Mon", 120)
    # h.get("Mon")
    # h["Mon"] = 120
    # h["Mon"]
    # print(h.arr)
    # print([[] * i for i in range(5)])
    h["Mon"] = 10
    h["Von"] = 20
    h["Con"] = 30
    h["Xon"] = 40
    h["won"] = 50
    h["qon"] = 60
    print(h['Xon'])
    del h['Xon']
    print(h.arr)
