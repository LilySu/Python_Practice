# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
#
# class LL:
#     def __init__(self):
#         self.head = None
#
#     def printll(self):
#         h = self.head
#         pstr = ''
#         while h:
#             pstr += str(h.data) + '-->'
#             h = h.next
#         print(pstr)
#
#     def add_to_beg(self, data):
#         if not self.head:
#             self.head = Node(data, None)
#             return
#         newNode = Node(data, self.head)
#         self.head = newNode
#
#     def get_len(self):
#         h = self.head
#         length = 0
#         while h:
#             length += 1
#             h = h.next
#         return length
#
#     def add_with_index(self, data, index):
#         if index < 0 or index > self.get_len():
#             raise Exception("Index out of Range")
#         counter = 0
#         p = self.head
#         while p:
#             if counter == index - 1:
#                 newNode = Node(data, p.next)
#                 p.next = newNode
#                 return
#             p = p.next
#             counter += 1
#
#     def delete_at_index(self, index):
#         if index < 0 or index > self.get_len():
#             raise Exception("Index out of Range")
#         counter = 0
#         p = self.head
#         while p:
#             if counter == index - 1:
#                 p.next = p.next.next
#                 break
#             p = p.next
#             counter += 1
#
# if __name__ == '__main__':
#     Linked = LL()
#     Linked.add_to_beg("Sun")
#     Linked.add_to_beg("Sat")
#     Linked.add_to_beg("Fri")
#     Linked.add_to_beg("Thur")
#     Linked.add_with_index("Added to index at 3", 3)
#     Linked.delete_at_index(1)
#     Linked.printll()


########################################################


#
# class Node:
#     def __init__(self, data, next):
#         self.data = data
#         self.next = next
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def printLL(self):
#         p = self.head
#         pstr = ''
#         while p:
#             pstr += str(p.data) + '-->'
#             p = p.next
#         print(pstr)
#
#     def get_len(self):
#         p = self.head
#         counter = 0
#         while p:
#             counter += 1
#             p = p.next
#         return counter
#
#     def add_beg(self, data):
#         if self.head == None:
#             self.head = Node(data, None)
#         else:
#             newNode = Node(data, self.head)
#             self.head = newNode
#
#     def add_at_idx(self, data, idx):
#         if idx < 0 or idx > self.get_len():
#             raise Exception("Index out of range")
#         if idx == 0:
#             newNode = Node(data, self.head)
#             self.head = newNode
#             return
#         p = self.head
#         counter = 0
#         while p:
#             if counter == idx - 1:
#                 newNode = Node(data, p.next)
#                 p.next = newNode
#             p = p.next
#             counter += 1
#
#     def delete_at_idx(self, idx):
#         if idx < 0 or idx > self.get_len():
#             raise Exception("Index out of range")
#         if idx == 0:
#             self.head = self.head.next
#             return
#         p = self.head
#         counter = 0
#         while p:
#             if counter == idx - 1:
#                 p.next = p.next.next
#                 return
#             p = p.next
#             counter += 1
#
# if __name__ == '__main__':
#     LL = LinkedList()
#     LL.add_beg("Sun")
#     LL.add_beg("Sat")
#     LL.add_beg("Fri")
#     LL.add_beg("Thur")
#     LL.add_at_idx("Inserted at index 2", 2)
#     LL.add_at_idx("Inserted at index 0", 0)
#     LL.delete_at_idx(3)
#     LL.printLL()



class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def printLL(self):
        pointer = self.head
        pstr = ''
        while pointer:
            pstr += str(pointer.data) + '-->'
            pointer = pointer.next
        print(pstr)

    def get_len(self):
        pointer = self.head
        counter = 0
        while pointer:
            counter += 1
            pointer = pointer.next
        return counter

    def insert_at_beg(self, data):
        if not self.head:
            self.head = Node(data, None)
        else:
            newNode = Node(data, self.head)
            self.head = newNode

    def insert_at_index(self, data, idx):
        if idx < 0 or idx > self.get_len():
            raise Exception("Index out of range")
        if idx == 0:
            self.head = Node(data, self.head)
            return
        pointer = self.head
        counter = 0
        while pointer:
            if counter == idx - 1:
                newNode = Node(data, pointer.next)
                pointer.next = newNode
                break
            pointer = pointer.next
            counter += 1

    def delete_at_idx(self, idx):
        if idx < 0 or idx > self.get_len():
            raise Exception("Index out of range")
        if idx == 0:
            self.head = self.head.next
            return
        pointer = self.head
        counter = 0
        while pointer:
            if counter == idx - 1:
                pointer.next = pointer.next.next
                break
            pointer = pointer.next
            counter += 1

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beg('Sun')
    ll.insert_at_beg('Mon')
    ll.insert_at_beg('Tue')
    ll.insert_at_beg('Wed')
    ll.insert_at_index('Inserted at index 2', 2)
    ll.insert_at_index('Inserted at index 0', 0)
    ll.delete_at_idx(0)
    ll.delete_at_idx(2)
    ll.printLL()
