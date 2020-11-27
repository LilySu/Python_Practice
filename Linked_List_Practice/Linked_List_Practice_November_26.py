class ListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        pstr = ""
        p = self.head
        while p:
            pstr += str(p.data) + '-->'
            p = p.next
        print(pstr)

    def get_length(self):
        length = 0
        p = self.head
        while p:
            length += 1
            p = p.next
        return length

    def insert_at_beg(self, data):
        newNode = ListNode(data, self.head)
        self.head = newNode

    def insert_at_index(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Index Out of Range")
        if index == 0:
            self.insert_at_beg(data)
            return
        counter = 0
        p = self.head
        while p:
            if counter == index - 1:
                newNode = ListNode(data, p.next)
                p.next = newNode
                break
            p = p.next
            counter += 1

    def del_at_index(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Index Out of Range")
        if index == 0:
            self.head = self.head.next
            return
        counter = 0
        p = self.head
        while p:
            if counter == index - 1:
                p.next = p.next.next
                break
            p = p.next
            counter += 1

if __name__ == '__main__':
    ll = LinkedList()

    ll.head = ListNode("Hea", None)
    ll.insert_at_beg("Madf")
    ll.insert_at_beg("Hdf")
    ll.insert_at_beg("Wer")
    ll.insert_at_beg("Po")
    ll.insert_at_beg("Qsu")
    ll.insert_at_beg("Jai")

    ll.insert_at_index(2, "Inserted at 2")
    ll.print_ll()
    ll.del_at_index(3)
    ll.print_ll()