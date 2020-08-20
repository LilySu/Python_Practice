class ListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head == None:
            print("Linked List is Empty")
        ptr = self.head
        pstr = ''
        while ptr:
            pstr += ptr.data + '-->'
            ptr = ptr.next
        print(pstr)

    def insert_beg(self, data):
        ptr = ListNode(data, self.head)
        self.head = ptr

    def get_len(self):
        len = 0
        ptr = self.head
        while ptr:
            len += 1
            ptr = ptr.next
        return len

    def insert_at_index(self, index, data):
        if index < 0 or index > self.get_len():
            raise Exception("Index out of range")
        if index == 0:
            self.insert_beg(data)
            return
        ptr = self.head
        counter = 0
        while ptr:
            if counter == index - 1:
                newNode = ListNode(data, ptr.next)
                ptr.next = newNode
            ptr = ptr.next
            counter += 1

    def delete_at_index(self, index):
        if index < 0 or index > self.get_len():
            raise Exception("Index out of range")
        if index == 0:
            self.head = self.head.next
            return
        ptr = self.head
        counter = 0
        while ptr:
            if counter == index - 1:
                ptr.next = ptr.next.next
            ptr = ptr.next
            counter += 1

if __name__ == '__main__':
    l = LinkedList()
    n = ListNode("Wed", None)
    m = ListNode("Tue", n)
    l.head = ListNode("Mon", m)
    l.print()
    l.insert_beg("Sun")
    l.insert_at_index(2, "Inserted Item")
    l.delete_at_index(1)
    l.print()



