class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, val):
        if val == self.data:
            return
        if val < self.data:
            if self.left:
                self.left.add_child(val)
            else:
                self.left = BST(val)
        else:
            if self.right:
                self.right.add_child(val)
            else:
                self.right = BST(val)

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
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

def build_tree(elements):
    root = BST(elements[0])
    for i in range(1, len(elements)):
        root.add_child(i)
    return root

if __name__ == '__main__':
    elements = [10, 17, 3, 4, 5, 6, 1, 2]
    tree = build_tree(elements)
    print(tree.traverse())
    print(tree.search(2))