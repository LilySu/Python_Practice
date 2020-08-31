class ListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def printll(self):
        p = self.head
        pstr = ''
        while p:
            pstr += '-->' + p.data
            p = p.next
        print(pstr)

    def insert_beg(self, data):
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
        if index <= 0 or index > self.get_len():
            raise Exception("Index Out of Range")
        p = self.head
        counter = 0
        while p:
            if counter == index - 1:
                newNode = ListNode(data, p.next)
                p.next = newNode
            counter += 1
            p = p.next

    def delete_at_index(self, index):
        if index <= 0 or index > self.get_len():
            raise Exception("Index Out of Range")
        p = self.head
        counter = 0
        while p:
            if counter == index - 1:
                p.next = p.next.next
            counter += 1
            p = p.next

if __name__=='__main__':
    l = LinkedList()
    l.head = ListNode("Mon", None)
    l.insert_beg("Don")
    l.insert_beg("Con")
    l.insert_beg("Xon")
    l.insert_at_index(3, "Inserted")
    l.delete_at_index(2)
    l.printll()