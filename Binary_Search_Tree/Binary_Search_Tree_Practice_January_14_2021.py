class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, value):
        if value == self.data:
            return
        elif value < self.data:
            if self.left:
                self.left.add_child(value)
            else:
                self.left = BST(value)
        else:
            if self.right:
                self.right.add_child(value)
            else:
                self.right = BST(value)

    def traverse(self):
        elements = []
        if self.left:
            elements += self.left.traverse()
        elements.append(self.data)
        if self.right:
            elements += self.right.traverse()
        return elements

    def search(self, value):
        if value == self.data:
            return True
        elif value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False

def build_tree(elements):
    root = BST(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == "__main__":
    elements = [1,2,3,4,5,6,7,8,9]
    tree = build_tree(elements)
    print(tree.traverse())
    tree.add_child(10)
    print(tree.traverse())
    print(tree.search(10))
        