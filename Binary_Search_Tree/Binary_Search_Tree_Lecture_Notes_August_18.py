class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        # check value first
        if data == self.data: # if value already exists
            return
        if data < self.data:
            # add data in left tree
            if self.left:
                self.left.add_child(data)
            else: # if left is empty
                self.left = BinarySearchTreeNode(data) # new tree node created
        else:
            # if value is greater than, add to right
            if self.right:
                self.right.add_child(data)
            else: # if left is empty
                self.right = BinarySearchTreeNode(data) # new tree node created

    # In order traversal
    def in_order_traversal(self):
        elements = []
        # fill all elements in a specific order
        # first visiting left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # visit base node, this particular node has value data, which I insert into it
        elements.append(self.data)
        # if the right side exists
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            # val might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False # this value does not exist in tree
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

if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(9)) # order log n search complexity
    # one of the utilities of a binary search tree is to sort
    # the other utility is to implement a set
    # O(n) insertion, O(n) deletion