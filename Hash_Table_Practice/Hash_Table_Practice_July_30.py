class Hash_Table():
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
                isfound = True
                break
        if isfound == False:
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
                del self.arr[h][index]

if __name__ == '__main__':
    t = Hash_Table()
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
    # print(t.arr)


# flink stream processing
# beam supports flink in runtime
# deploy flink as an application
# when on prem flink is execution on top
# pulsar vs flink
# batch storage hdfs, s3
# batch computer - spark, hive
# pulsar, kafka - on storage side of things
# streaming equivalent of hdfs/s3
# flink: computation - spark, mapreduce, hive
# flink approvement proposals shows extended support for python

# agregation, scalar vs table functions vs what environments - ie access to native libraries,
# interplay with other libraries and api's like pandas