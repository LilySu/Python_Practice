class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        printobj = self.head
        while printobj:
            print(printobj.data)
            printobj = printobj.next

    def insert_beg(self, data):
        newNode = Node(data, self.head)
        self.head = newNode

    def get_length(self):
        counter = 0
        pointer = self.head
        while pointer:
            counter += 1
            pointer = pointer.next
        return counter

    def insert_at_index(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Index out of Range")
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
            counter += 1

if __name__=='__main__':
    l = LinkedList()
    l.head = Node("Mon", None)
    l.insert_beg("Don")
    l.insert_beg("Con")
    l.insert_beg("Xon")
    l.insert_at_index(3, "Inserted")
    l.print()