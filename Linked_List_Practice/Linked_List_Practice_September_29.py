class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("linked list empty")
            return
        ptr = self.head
        print_str = ''
        while ptr:
            print_str += str(ptr.data) + '-->'
            ptr = ptr.next
        print(print_str)

    def insert_beg(self, value):
        node = Node(value, self.head)
        self.head = node

    def insert_end(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = Node(value, None)

    def length(self):
        count = 0
        ptr = self.head
        while ptr:
            count += 1
            ptr = ptr.next
        return count

    def remove_at(self, index):
        if index < 0 or index > self.length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        ptr = self.head
        while ptr:
            if count == index - 1:
                ptr.next = ptr.next.next
                break
            ptr = ptr.next
            count += 1

    def insert_at(self, index, value):
        if index < 0 or index > self.length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_beg(value)
            return
        count = 0
        ptr = self.head
        while ptr:
            if count == index - 1:
                node = Node(value, ptr.next)
                ptr.next = node
                break
            ptr = ptr.next
            count += 1

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_beg("Mon")
    ll.insert_beg("Tue")
    ll.insert_end("Wed")
    ll.insert_at(2, "Inserted item")
    ll.remove_at(3)
    ll.print_ll()
