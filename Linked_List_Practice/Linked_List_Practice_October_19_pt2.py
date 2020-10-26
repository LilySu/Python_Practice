class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        p = self.head
        pstr = ""
        while p:
            pstr += str(p.data) + "-->"
            p = p.next
        print(pstr)

    def get_len(self):
        p = self.head
        counter = 0
        while p:
            counter += 1
            p = p.next
        return counter

    def insert_at_beg(self, data):
        newNode = Node(data, self.head)
        self.head = newNode

    def insert_at_index(self, index, data):
        if index < 0 or index > self.get_len():
            raise Exception("Index out of bounds")
        if index == 0:
            self.insert_at_beg(data)
        p = self.head
        counter = 0
        while p:
            if counter == index - 1:
                newNode = Node(data, p.next)
                p.next = newNode
                break
            p = p.next
            counter += 1

    def delete_at_index(self, index):
        if index < 0 or index > self.get_len():
            raise Exception("Index out of bounds")
        if index == 0:
            self.head = self.head.next
            return
        p = self.head
        counter = 0
        while p:
            if counter == index - 1:
                p.next = p.next.next
            p = p.next
            counter += 1

if __name__ == "__main__":
    l = LinkedList()
    l.insert_at_beg("Mon")
    l.insert_at_beg("Bon")
    l.insert_at_beg("Con")
    l.insert_at_beg("Don")
    l.insert_at_index(1, "Inserted")
    l.delete_at_index(3)
    l.print()