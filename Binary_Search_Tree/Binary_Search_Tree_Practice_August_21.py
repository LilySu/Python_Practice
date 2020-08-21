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
        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

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

    def find_max(self):
        if self.right:
            self.right.find_max()
        else:
            return self.data

    def find_min(self):
        if self.left is None:
            return self.data
        else:
            self.left.find_min()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data  = min_val
            self.right = self.right.delete(min_val)
        return self

def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    t = build_tree(numbers)
    print(t.traverse())
    print(t.search(20))

    t.delete(4)
    print(t.traverse())

