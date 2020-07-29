class ListNode:
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
            printstr += printobj.data + '-->'
            printobj = printobj.next
        print(printstr)

    def insert_beg(self, data):
        newNode = ListNode(data, self.head)
        self.head = newNode

    def get_length(self):
        counter = 0
        pointer = self.head
        while pointer:
            counter += 1
            pointer = pointer.next
        return counter

    def remove_at_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Index out of range")
        if self.head is None:
            return
        if index == 0:
            self.head = self.head.next
        counter = 0
        pointer = self.head
        while pointer:
            if counter == index - 1:
                pointer.next = pointer.next.next
            pointer = pointer.next
            counter += 1

    def insert_at_index(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Index out of range")
        if index == 0:
            self.insert_beg(data)
        counter = 0
        pointer = self.head
        while pointer:
            if counter == index - 1:
                newNode = ListNode(data, pointer.next)
                pointer.next = newNode
            pointer = pointer.next
            counter += 1


if __name__ == '__main__':
    ll = LinkedList()
    llc = ListNode('Cheese', None)
    llb = ListNode('Bacon', llc)
    lla = ListNode('Tofu', llb)
    ll.head = ListNode('Crossant', lla)

    ll.insert_beg('Egg')
    ll.remove_at_index(4)
    ll.insert_at_index(4, 'Pizza')

    ll.print()
