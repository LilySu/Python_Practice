class Node:
    def __init__(self, data , next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def printll(self):
        if self.head is None:
            print("linked list empty")
            return
        p = self.head
        pstr = ''
        while p:
            pstr += str(p.data) + '-->'
            # print(p.data)
            p = p.next
        print(pstr)

    def get_len(self):
        l = 0
        p = self.head
        while p:
            l += 1
            p = p.next
        return l

    def insert_beg(self, data):
        newNode = Node(data, self.head)
        self.head = newNode

    def insert_at_index(self, index, data):
        if index < 0 and index >= self.get_len():
            raise Exception('Index out of range')
        if index == 0:
            self.insert_beg(data)
        c = 0
        p = self.head
        while p:
            if c == index - 1:
                newNode = Node(data, p.next)
                p.next = newNode
            p = p.next
            c += 1

    def remove_at_index(self, index):
        if index < 0 or index >= self.get_len():
            raise Exception("Index out of range")
        if index == 0:
            self.head = self.head.next
            return
        c = 0
        p = self.head
        while p:
            if c == index -1:
                p.next = p.next.next
            p = p.next
            c += 1

if __name__ == '__main__':
    l = LinkedList()
    l2 = Node("Wed", None)
    l1 = Node("Tue", l2)
    l.head = Node("Mon", l1)

    l.insert_beg("Sun")
    l.insert_at_index(2, "Inserted item")
    l.remove_at_index(0)

    l.printll()
