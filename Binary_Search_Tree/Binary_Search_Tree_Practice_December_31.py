class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        elif data < self.data:
            if self.left:
                self.left.add_child(data)
            if not self.left:
                self.left = BinarySearchTree(data)
        elif data > self.data:
            if self.right:
                self.right.add_child(data)
            if not self.right:
                self.right = BinarySearchTree(data)

    def search(self, data):
        if data == self.data:
            return True
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def traverse(self):
        elements = []
        if self.left:
            elements += self.left.traverse()
        elements.append(self.data)
        if self.right:
            elements += self.right.traverse()
        return elements

def build_tree(elements):
    r = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        r.add_child(elements[i])
    return r
if __name__ == '__main__':
    elements = [87, 2, 49, 14, 62]
    r = build_tree(elements)
    print(r.traverse())
    print(r.search(2))
    print(r.search(3))
    r.add_child(30)
    print(r.traverse())
