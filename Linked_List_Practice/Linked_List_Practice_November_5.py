class ListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def printll(self):
        pstr = ""
        p = self.head
        while p:
            pstr += "-->" + str(p.data)
            p = p.next
        print(pstr)

    def get_len(self):
        p = self.head
        counter = 0
        while p:
            p = p.next
            counter += 1
        return counter

    def insert_beg(self, data):
        newNode = ListNode(data, self.head)
        self.head = newNode

    def insert_at_index(self, index, data):
        if index < 0 or index > self.get_len():
            raise Exception("Index out of bounds")
        if index == 0:
            self.insert_beg(data)
            return
        p = self.head
        counter = 0
        while p:
            if counter == index - 1:
                newNode = ListNode(data, p.next)
                p.next = newNode
                break
            p = p.next
            counter += 1

    def del_at_index(self, index):
        if index < 0 or index > self.get_len():
            raise Exception("Index out of bounds")
        if index == 0:
            self.head = self.head.next
            return
        p = self.head
        counter = 0
        while p:
            if counter == index - 1:
                p.next = p.next.next
                break
            p = p.next
            counter += 1



if __name__=='__main__':
    l = LinkedList()
    l.head = ListNode("Mon", None)
    l.insert_beg("Don")
    l.insert_beg("Con")
    l.insert_beg("Xon")
    l.insert_at_index(3, "Inserted")
    l.del_at_index(2)
    l.printll()