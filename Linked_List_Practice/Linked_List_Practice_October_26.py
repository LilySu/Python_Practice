class ListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def get_len(self):
        p = self.head
        counter = 0
        while p:
            p = p.next
            counter += 1
        return counter

    def print_ll(self):
        p = self.head
        pstr = ""
        while p:
            pstr += str(self.data) + "-->"
            p = p.next
        print(pstr)

    def insert_beg(self, data):
        newNode = ListNode(data, self.head)
        self.head = newNode

    def insert_at_index(self, index, data):
        if index < 0 or index >= self.get_len():
            raise Exception("index out of bounds")
        if index == 0:
            self.insert_beg(data)
        p = self.head
        counter = 0
        while p:
            if counter == index - 1:
                newNode = ListNode(data, p.next)
                p.next = newNode
            p = p.next
            counter += 1

    def del_at_index(self, index):
        if index < 0 or index >= self.get_len():
            raise Exception("index out of bounds")
        p = self.head
        counter = 0
        while p:
            if counter == index - 1:
                p.next = p.next.next
            p = p.next
            counter += 1

