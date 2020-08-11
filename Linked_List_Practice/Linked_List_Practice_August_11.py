class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None

    def print(self):
        pointer = self.head
        pstr = ''
        while pointer:
            pstr += str(pointer.data) + '  '
            pointer = pointer.next
        print(pstr)

    def insert_beg(self, data):
        newNode = Node(data, self.head)
        self.head = newNode

    def get_length(self):
        length = 0
        pointer = self.head
        while pointer:
            length += 1
            pointer = pointer.next
        return length

    def insert_at_index(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Index out of bounds")
        if index == 0:
            self.insert_beg(data)
        counter = 0
        pointer = self.head
        while pointer:
            if counter == index - 1:
                newNode = Node(data, pointer.next)
                pointer.next = newNode
                break
            pointer = pointer.next
            counter += 1

    def delete_at_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Index out of bounds")
        if index == 0:
            self.head = self.head.next
        counter = 0
        pointer = self.head
        while pointer:
            if counter == index - 1:
                pointer.next = pointer.next.next
                break
            pointer = pointer.next
            counter += 1

if __name__ == '__main__':
    l = Linked_List()
    c = Node("don", None)
    b = Node("con", c)
    a = Node("bon", b)
    l.head = Node("mon", a)
    l.insert_at_index(1, "pizza")
    l.delete_at_index(2)
    l.print()