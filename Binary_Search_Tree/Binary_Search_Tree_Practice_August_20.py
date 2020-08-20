class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_item(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_item(data)
            else:
                self.left = BST(data)
        if data > self.data:
            if self.right:
                self.right.add_item(data)
            else:
                self.right = BST(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def search(self, val):
        if self.data == val:
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
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_max()

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
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self


def build_tree(elements):
    root = BST(elements[0])
    for i in range(1, len(elements)):
        root.add_item(elements[i])
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    t = build_tree(numbers)
    print(t.in_order_traversal())
    print(t.search(20))

    t.delete(4)
    print(t.in_order_traversal())
