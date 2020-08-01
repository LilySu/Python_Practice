class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        printobj = self.head
        printstr = ''
        while printobj:
            printstr += str(printobj.data) + '-->'
            printobj = printobj.next
        return printstr

    def get_length(self):
        counter = 0
        pointer = self.head
        while pointer:
            pointer = pointer.next
            counter += 1
        return counter

    def insert_beg(self, data):
        newNode = Node(data, self.head)
        self.head = newNode

    def insert_at_index(self, index, data):
        if index < 0 and index > self.get_length():
            raise Exception("Index out of range")
        if index == 0:
            self.insert_beg(data)
            return
        counter = 0
        pointer = self.head
        while pointer:
            if counter == index - 1:
                newNode = Node(data, pointer.next)
                pointer.next = newNode
                break
            pointer = pointer.next
            counter +=  1