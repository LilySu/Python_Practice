class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LL:
    def __init__(self):
        self.head = None

    def print_ll(self):
        pstr = ''
        pstr = self.head
        while p:
            pstr += str(self.data) + '-->'
            p = p.next
        print(pstr)

    def add_in_beg(self, val):
        if not self.head:
            self.head = val
        newNode = Node(val, self.head)
        self.head = newNode

    def get_len(self):
        p = self.head
        counter = 0
        while p:
            counter += 1
            p = p.next
        return counter

    def add_ind(self, idx, val):
        if idx < 0 and idx > self.get_len():
            raise Exception('Index out of Range')
        p = self.head
        count =0
        while p:
            if 