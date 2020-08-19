class BinarySearchTreeNode:
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
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def traverse(self):
        elements = []
        if self.left:
            elements += self.left.traverse()
        elements.append(self.data)
        if self.right:
            elements += self.right.traverse()
        return elements

    def search(self, val):
        if val == self.data:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

def build_tree(elements):
    bst = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        bst.add_child(i)
    return bst

if __name__ == '__main__':
    elements = [17, 6, 20, 88, 9, 0, 2]
    numbers_tree = build_tree(elements)
    print(numbers_tree.traverse())
    print(numbers_tree.search(6))
    print(numbers_tree.add_child(10))
    print(numbers_tree.traverse())
