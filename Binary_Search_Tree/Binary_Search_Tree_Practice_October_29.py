class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                return self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
