class invertedBT():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_children(self, child):
        if child == self.data:
            return
        if child > self.data:
            if self.left:
                self.left.add_children(child)
            else:
                self.left = invertedBT(child)
        if child < self.data:
            if self.right:
                self.right.add_children(child)
            else:
                self.right = invertedBT(child)

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
            if self.right:
                return self.right.search(val)
            else:
                return False
        if val > self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

def build_tree(elements):
    root = invertedBT(elements[0])
    for i in range(1, len(elements)):
        root.add_children(elements[i])
    return root

if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    t = build_tree(numbers)
    print(t.traverse())
    pass