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

    def traverse_tree(self):
        elements = []
        if self.left:
            # return list, add list to existing
            elements += self.left.traverse_tree()
        # when there is nothing on the left, add
        elements.append(self.data)
        # shift 1 to the right and add to elements again
        if self.right:
            elements += self.right.traverse_tree()
        return elements

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

def build_tree(elements):
    r = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        r.add_child(elements[i])
    return r

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    t = build_tree(numbers)
    print(t.traverse_tree())
    print(t.search(20))


    print(t.traverse_tree())