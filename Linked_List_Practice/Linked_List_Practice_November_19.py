class ListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        p = self.head
        pstr = ""
        while p:
            pstr += str(p.data) + "-->"
            p = p.next
        print(pstr)

    def get_length(self):
        length = 0
        p = self.head
        while p:
            length += 1
            p = p.next
        return length

    def insert_to_beg(self, data):
        newNode = ListNode(data, self.head)
        self.head = newNode

    def insert_to_index(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Index out of range")
        if index == 0:
            self.insert_to_beg(data)
            return
        counter = 0
        p = self.head
        while p:
            if counter == (index - 1):
                newNode = ListNode(data, p.next)
                p.next = newNode
            p = p.next
            counter += 1

    def del_at_index(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Index out of range")
        if index == 0:
            self.head = self.head.next
        counter = 0
        p = self.head
        while p:
            if counter == (index - 1):
                p.next = p.next.next
            p = p.next
            counter += 1

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_to_beg("Aas")
    ll.insert_to_beg("skl")
    ll.insert_to_beg("Aew")
    ll.insert_to_beg("Acx")
    ll.insert_to_beg("Aa")
    ll.insert_to_beg("Auy")
    ll.insert_to_index(2, "Inserted at 2nd index")
    ll.del_at_index(4)

    ll.print_LL()
