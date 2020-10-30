class ListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def get_len(self):
        p = self.head
        counter = 0
        while p:
            counter += 1
            p = p.next
        return counter

    def printll(self):
        if self.head == None:
            print("Linked List Empty")
            return
        p = self.head
        pstr = ""
        while p:
            pstr += str(p.data) + "-->"
            p = p.next
        print(pstr)

    def insert_beg(self, data):
        newNode = ListNode(data, self.head)
        self.head = newNode

    def insert_at_index(self, index, data):
        if index < 0 or index > self.get_len():
            raise Exception("Index out of range")
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
            counter += 1
            p = p.next

    def delete_at_index(self, index):
        if index < 0 or index > self.get_len():
            raise Exception("Index out of range")
        if index == 0:
            self.head = self.head.next
            return
        p = self.head
        counter = 0
        while p:
            if counter == index - 1:
                p.next = p.next.next
            counter += 1
            p = p.next

if __name__ == "__main__":
    l = LinkedList()
    l.insert_beg("Mon")
    l.insert_beg("Bon")
    l.insert_beg("Con")
    l.insert_beg("Don")
    l.insert_at_index(1, "Inserted")
    # l.delete_at_index(3)
    l.printll()