# because binary search trees do not store duplicates
# it is a great way to implement sets
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data: # check value first, the data that I am adding if the value already exists
            # then you don't need to add elements, Binary Tree does not have duplicates
            return
        if data < self.data:
            # add this value, data in left subtree
            # if your left element already has a value, which means you are not a leaf node
            if self.left:
                self.left.add_child(data) # recursively call add_child to continue to check to see
                # where the value, data should fit
            else: # your left node is empty
                self.left = BinarySearchTreeNode(data) #recursion
        else: # value is greater than, then
            # add value in right
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    # in order traversal method to print all elements in tree in ascending order
    def in_order_traversal(self):
        elements = []

        # visit left tree first
        if self.left:
            elements += self.left.in_order_traversal() # returns some list to add to the elements list

        # then visit base node
        elements.append(self.data) # this node has a node name data that I want to append to the elements list

        # then visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            # val might be in left subtree
            if self.left: # do I have any content in left subtree
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            # val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__=='__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(11))