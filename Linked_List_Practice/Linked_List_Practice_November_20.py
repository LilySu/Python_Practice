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

    def insert_beg(self, info):
        newNode = ListNode(info, self.head)
        self.head = newNode

    def get_length(self):
        length = 0
        p = self.head
        while p:
            length += 1
            p = p.next
        return length

    def insert_at_index(self, index, info):
        if index < 0 or index > self.get_length():
            raise Exception("Index out of range")
        if index == 0:
            self.insert_beg(info)
            return
        counter = 0
        p = self.head
        while p:
            if counter == index - 1:
                newNode = ListNode(info, p.next)
                p.next = newNode
                break
            p = p.next
            counter += 1

    def del_at_index(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Index out of range")
        if index == 0:
            self.head = self.head.next
            return
        counter = 0
        p = self.head
        while p:
            if counter == index - 1:
                p.next = p.next.next
            p = p.next
            counter += 1

if __name__ == "__main__":
    l = LinkedList()
    l.insert_beg("a")
    l.insert_beg("ab")
    l.insert_beg("abc")
    l.insert_beg("abcd")
    l.insert_beg("abcde")
    l.insert_beg("abcdef")
    l.insert_at_index(3, "inserted at index 3")
    l.del_at_index(1)
    l.print_ll()


