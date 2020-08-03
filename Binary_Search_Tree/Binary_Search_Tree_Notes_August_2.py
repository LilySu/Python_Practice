# one way to implement a set is to use a binary search tree
# a binary tree has max 2 nodes
# binary search tree elements have some sort of order

# because the search space is reduced by half in each iteratation
# search complexity is log(base 2) or O(log n)

# Use cases
# 1. sort elements
# 2. implement class, so as to remove duplicates

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # left subtree is always less
    def add_child(self, data):
        if data == self.data: # if value already exists
            return # don't add anything, there are no duplicates
        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self): # fill list of all elements in bst in order
        elements = []
        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # visit base node
        elements.append(self.data)
        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val): # O(log(n)) search complexity
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False # this value does not exist
        if val > self.data:
            # val might be in right
            if self.right:
                return self.right.search(val)
            else:
                return False

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(200))
