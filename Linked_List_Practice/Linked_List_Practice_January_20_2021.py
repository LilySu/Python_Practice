class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def get_len(self):
        pointer = self.head
        length = 0
        while pointer:
            length += 1
            pointer = pointer.next
        return length

    def print_ll(self):
        pointer = self.head
        pstr = ""
        while pointer:
            pstr += str(pointer.val) + "-->"
            pointer = pointer.next
        print(pstr)

    def insert_beg(self, data):
        if self.head is None:
            self.head = ListNode(data, None)
        else:
            newNode = ListNode(data, self.head)
            self.head = newNode

    def insert_data_at_idx(self, idx, data):
        if idx < 0 or idx > self.get_len():
            raise Exception("Index Out of Range")
        counter = 0
        pointer = self.head
        while pointer:
            if counter == idx - 1:
                newNode = ListNode(data, pointer.next)
                pointer.next = newNode
                break
            pointer = pointer.next
            counter += 1

    def delete_at_idx(self, idx):
        if idx < 0 or idx > self.get_len():
            raise Exception("Index Out of Range")
        if idx == 0:
            self.head = self.head.next
            return
        counter = 0
        pointer = self.head
        while pointer:
            if counter == idx - 1:
                pointer.next = pointer.next.next
                break
            pointer = pointer.next
            counter += 1

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_beg('Sun')
    ll.insert_beg('Sat')
    ll.insert_beg('Fri')
    ll.insert_beg('Thur')
    ll.print_ll()
    ll.insert_beg('Wed')
    ll.print_ll()
    ll.insert_data_at_idx(2, 'Pixie inserted at index 2')
    ll.print_ll()
    ll.delete_at_idx(0)
    ll.print_ll()