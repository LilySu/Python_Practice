class ListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head  = None

    def print_ll(self):
        p = self.head
        pstr = ''
        while p:
            pstr += str(p.data) + '-->'
            p = p.next
        return pstr

    def add_beg(self, data):
        newNode = ListNode(data, self.head)
        self.head = newNode

    def get_len(self):
        p = self.head
        counter = 0
        while p:
            counter += 1
            p = p.next
        return counter

    def insert_at_index(self, index, data):
        if index < 0 or index > self.get_len():
            raise Exception("Index out of Range")
        p = self.head
        counter = 0
        while p:
            if counter == index - 1:
                newNode = ListNode(data, p.next)
                p.next = newNode
                break
            counter += 1
            p = p.next

    def delete_at_index(self, index):
        if index < 0 or index > self.get_len():
            raise Exception("Index out of Range")
        p = self.head
        counter = 0
        while p:
            if counter == index - 1:
                p.next = p.next.next
            counter += 1
            p = p.next

if __name__ == '__main__':
    l = LinkedList()
    l.add_beg("Sat")
    l.add_beg("Fri")
    l.add_beg("Thur")
    l.add_beg("Wed")
    l.add_beg("Tue")
    l.add_beg("Mon")
    print(l.print_ll())
    l.insert_at_index(3,"inserted at index 3")
    print(l.print_ll())
    l.delete_at_index(1)
    print(l.print_ll())