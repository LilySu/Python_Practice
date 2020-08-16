class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = head

    def print(self):
        pobj = self.head
        pstr = ''
        while pobj:
            pstr += pstr.data
            pobj = pobj.next
        return pstr

    def insert_beg(self, data):
        newNode = Node(data, self.head)
        self.head = newNode

    def get_len(self):
        len = 0
        pointer = self.head
        while pointer:
            len += 1
            pointer = pointer.next
        return len

    def insert_index_value(self, index, value):
        if index < 0 or index > self.get_len():
            raise Exception("Index out of Bounds")
        if index == 0:
            self.insert_beg(data)
            return
        pointer = self.head
        counter = 0
        while pointer:
            if counter == index - 1:
                newNode = Node(data, pointer.next)
                pointer.next = newNode
                break
            pointer = pointer.next
            counter += 1

    def remove_at(self, index):
        if index < 0 or index > self.get_len():
            raise Exception("Index out of Bounds")
        if index == 0:
            self.head = self.head.next
            return
        pointer = self.head
        counter = 0
        while pointer:
            if counter == index - 1:
                pointer.next = pointer.next.next
                break
            pointer = pointer.next
            counter += 1