class ListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        p = self.head
        pstr = ''
        while p:
            pstr += p.data + '-->'
            p = p.next
        print(pstr)

    def get_len(self):
        p = self.head
        count = 0
        while p:
            count += 1
            p = p.next
        return count

    def insert_beg(self, data):
        newNode = ListNode(data, self.head)
        self.head = newNode

    def insert_at_index(self, index, data):
        if index > self.get_len() or index < 0:
            raise Exception("Index out of range")
        if index == 0:
            self.insert_beg(data)
        p = self.head
        counter = 0
        while p:
            if counter == (index - 1):
                newNode = ListNode(data, p.next)
                p.next = newNode
                break
            p = p.next
            counter += 1

    def delete_at_index(self, index):
        if index > self.get_len() or index < 0:
            raise Exception("Index out of range")
        p = self.head
        counter = 0
        while p:
            if counter == (index - 1):
                p.next = p.next.next
                break
            p = p.next
            counter += 1

if __name__ == "__main__":
    l = LinkedList()
    l.insert_beg("Mon")
    l.insert_beg("Bon")
    l.insert_beg("Con")
    l.insert_beg("Don")
    l.insert_at_index(1, "Inserted")
    l.delete_at_index(2)
    l.print()
