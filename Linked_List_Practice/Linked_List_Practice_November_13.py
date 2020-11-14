class ListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def printll(self):
        p = self.head
        pstr = ""
        while p:
            pstr += str(p.data) + "-->"
            p = p.next
        print(pstr)

    def add_to_beg(self, data):
        newNode = ListNode(data, self.head)
        self.head = newNode

    def get_len(self):
        counter = 0
        p = self.head
        while p:
            counter += 1
            p = p.next
        return counter

    def insert_at_index(self, index, data):
        if index < 0 and index > self.get_len():
            raise Exception("Index out of bounds")
        if index == 0:
            self.add_to_beg(data)
            return
        p = self.head
        count = 0
        while p:
            if count == index - 1:
                newNode = ListNode(data, p.next)
                p.next = newNode
                break
            p = p.next
            count += 1

    def delete_at_index(self, index):
        if index < 0 and index > self.get_len():
            raise Exception("Index out of bounds")
        if index == 0:
            self.head = self.head.next
            return
        p = self.head
        count = 0
        while p:
            if count == index - 1:
                p.next = p.next.next
                break
            p = p.next
            count += 1

if __name__ == "__main__":
    l = LinkedList()
    l.head = ListNode("Thur", None)
    l.add_to_beg("Wed")
    l.add_to_beg("Tue")
    l.add_to_beg("Mon")
    l.add_to_beg("Sun")
    l.add_to_beg("Sat")
    l.insert_at_index(3, "Inserted at Index")
    l.delete_at_index(1)
    l.printll()
