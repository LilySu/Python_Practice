class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LL:
    def __init__(self):
        self.head = None

    def add_to_beg(self, data):
        if not self.head:
            self.head = Node(data, None)
            return
        newNode = Node(data, self.head)
        self.head = newNode

    def get_len(self):
        p = self.head
        counter = 0
        while p:
            p = p.next
            counter += 1
        return counter

    def print_ll(self):
        p = self.head
        pstr = ''
        while p:
            pstr += str(p.data) + '-->'
            p = p.next
        print(pstr)

    def insert_at_index(self, index, data):
        if index > self.get_len() or index < 0:
            raise Exception("Index Out of Range")
        counter = 0
        p = self.head
        while p:
            if counter == index - 1:
                newNode = Node(data, p.next)
                p.next = newNode
                break
            p = p.next
            counter += 1

    def delete_at_index(self, index):
        if index > self.get_len() or index < 0:
            raise Exception("Index Out of Range")
        counter = 0
        p = self.head
        while p:
            if counter == index - 1:
                p.next = p.next.next
                break
            p = p.next
            counter += 1

if __name__ == '__main__':
    l = LL()
    l.add_to_beg("Wed")
    l.add_to_beg("Tue")
    l.add_to_beg("Mon")
    l.add_to_beg("Sun")
    l.add_to_beg("Sat")
    l.insert_at_index(2, "Inserted at 2")
    l.print_ll()
    l.delete_at_index(1)
    l.print_ll()