class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)

    def traverse_tree(self):
        elements = []
        if self.left:
            elements += self.left.traverse_tree()
        elements.append(self.data)
        if self.right:
            elements += self.right.traverse_tree()
        return elements

    def search(self, data):
        if data == self.data:
            return True
        elif data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        else:
            if self.right:
                return self.right.search(data)
            else:
                return False

def build_tree(elements):
    r = BST(elements[0])
    for i in range(1, len(elements)):
        r.add_child(elements[i])
    return r

if __name__ == "__main__":
    elements = [294, 18, 98, 65, 2]
    tree = build_tree(elements)
    print(tree.traverse_tree())
    print(tree.search(17))