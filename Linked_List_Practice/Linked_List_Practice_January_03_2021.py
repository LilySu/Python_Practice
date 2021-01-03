class LLNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LinkedList(self):
        p = self.head
        pstr = ""
        while p:
            pstr += str(p.data) + "-->"
            p = p.next
        print(pstr)

    def add_to_beg(self, data):
        newNode = LLNode(data, self.head)
        self.head = newNode

    def get_len(self):
        length = 0
        p = self.head
        while p:
            length += 1
            p = p.next
        return length

    def add_to_index(self, index, data):
        if index < 0 or index > self.get_len():
            raise Exception("Index Out of Range")
        counter = 0
        p = self.head
        while p:
            if counter == (index - 1):
                newNode = LLNode(data, p.next)
                p.next = newNode
                break
            counter += 1
            p = p.next

    def del_at_index(self, index):
        if index < 0 or index > self.get_len():
            raise Exception("Index Out of Range")
        counter = 0
        p = self.head
        while p:
            if counter == (index - 1):
                p.next = p.next.next
                break
            counter += 1
            p = p.next

if __name__ == '__main__':
    l = LinkedList()
    l.head = LLNode("Mon", None)
    l.add_to_beg("Sun")
    l.add_to_beg("Sat")
    l.add_to_beg("Fri")
    l.print_LinkedList()
    l.add_to_index(1, "Inserted at Index of 1")
    l.print_LinkedList()
    l.del_at_index(3)
    l.print_LinkedList()