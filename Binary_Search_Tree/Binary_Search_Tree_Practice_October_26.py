class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            # if value already exists, don't add anything
            return
        # if value doesn't exist
        if data < self.data: # value less than current node
            # add data in left of tree
            # check if left element has some value
            if self.left:
                self.left.add_child(data) # recursively call add child method
            else: # if left node is empty
                # create new node on left
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in right tree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        # return items in binary tree in sorted order
        elements = []
        # fill list by checking the left first
        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # visit base node
        elements.append(self.data)
        #visit right tree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

# helper method to build tree
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0]) # assign root node
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__=='__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    # utilities of binary search tree
    #  - sort elements
    #  - implement set class where elements appear only once



class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)



    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)
