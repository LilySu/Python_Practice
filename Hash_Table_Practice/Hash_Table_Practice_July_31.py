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
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, value)
                break
        if isfound is False:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h]


if __name__ == '__main__':
    t = HashTable()
    t['Ab'] = 23
    t['as'] = 14
    t['67'] = 1
    t['eri'] = 86
    t['Ar'] = 23
    t['ag'] = 14
    t['6h'] = 1
    t['erq'] = 86
    # print(t.arr)
    # del t['Ar']
    print(t['ag'])