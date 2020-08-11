class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def printl(self):
        pointer = self.head
        pstr = ''
        while pointer:
            pstr += str(pointer.data) + '-->'
            pointer = pointer.next
        print(pstr)

    def insert_beg(self, data):
        newNode = Node(data, self.head)
        self.head = newNode

    def get_length(self):
        counter = 0
        pointer = self.head
        while pointer:
            pointer = pointer.next
            counter += 1
        return counter

    def insert_at_index(self, index, data):
        if index < 0 and index >= self.get_length():
            raise Exception("Index out of range")
        if index == 0:
            self.insert_beg(data)
        counter = 0
        pointer = self.head
        while pointer:
            if counter == index - 1:
                newNode = Node(data, pointer.next)
                pointer.next = newNode
            pointer = pointer.next
            counter += 1

    def remove_at_index(self, index):
        if index < 0 and index >= self.get_length():
            raise Exception("Index out of range")
        if index == 0:
            self.head = self.head.next
        counter = 0
        pointer = self.head
        while pointer:
            if counter == index - 1:
                pointer.next = pointer.next.next
            pointer = pointer.next
            counter += 1

if __name__ == '__main__':
    l = LinkedList()
    l3 = Node("Thur", None)
    l2 = Node("Wed", l3)
    l1 = Node("Tue", l2)
    l.head = Node("Mon", l1)

    l.insert_at_index(0, "Inserted")
    # l.remove_at_index(0)

    l.printl()

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_index(self, index, data):
        if index < 0 and index >= self.get_length():
            raise Exception("Index out of range")
        if index == 0:
            self.insert_beg(data)
        pointer = self.head
        counter = 0
        while pointer:
            if counter == index - 1:
                newNode = Node(data, pointer.next)
                pointer.next = newNode
            pointer = pointer.next
            counter += 1
