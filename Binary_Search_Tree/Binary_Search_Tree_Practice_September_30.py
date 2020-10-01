class BSTNode:
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
                self.left = BSTNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTNode(data)

    def in_order_traversal(self):
        elements = [] # return elements in binary tree in order
        # visit left tree
        if self.left: # if in left hand you have elements
            elements += self.left.in_order_traversal()
        # visit base node
        elements.append(self.data) # this node has value data, for which we insert elements
        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            # val might be in left tree
            if self.left:
                return self.left.search(val)
            else: # reached end
                return False
        if val > self.data:
            # val might be in right tree
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
        return self.left.find_min()

    def delete(self, val):
        if val < self.data: # if value is less than the current node
            if self.left:
                self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self

def build_tree(elements):
    root = BSTNode(elements[0]) # assign first element as root node
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    numbers_tree.delete(20)
    print(numbers_tree.in_order_traversal())