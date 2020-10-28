class ListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def printll(self):
        p = self.head
        result = ""
        while p:
            result += str(p.data) + "-->"
            p = p.next
        print(result)

    def insert_beg(self, data):
        newNode = ListNode(data, self.head)
        self.head = newNode

    def lengthll(self):
        p = self.head
        counter = 0
        while p:
            counter += 1
            p = p.next
        return counter

    def insert_at_index(self, index, data):
        if index < 0 or index > self.lengthll():
            raise Exception("Index out of range")
        if index == 0:
            return self.insert_beg(data)
        p = self.head
        counter = 0
        while counter < index - 1:
            newNode = ListNode(data, p.next)
            p.next = newNode
            p = p.next
            counter += 1

    def delete_at_index(self, index):
        if index < 0 or index > self.lengthll():
            raise Exception("Index out of range")
        p = self.head
        counter = 0
        while counter < index - 1:
            p.next = p.next.next
            p = p.next
            counter += 1

if __name__ == "__main__":
    l = LinkedList()
    l.insert_beg("Mon")
    l.insert_beg("Bon")
    l.insert_beg("Con")
    l.insert_beg("Don")
    l.insert_at_index(1, "Inserted")
    # l.delete_at_index(3)
    l.printll()