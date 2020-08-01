class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data: # if the value already exists, don't add
            return# binary search tree does not have duplicate elements
        if data < self.data:
            # add data in left subtree
            if self.left: # does the left side already have values
                self.left.add_child(data)
            else:
                self.left = Tree(data)
        else: # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Tree(data)

    def in_order_traversal(self): # print tree in order
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # visit base node
        elements.append(self.data)
        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            # val might be in left subtree
            if self.left: # do I have any content on the left
                return self.left.search(val)
            else: # if no value exists in tree
                return False
        if val > self.data:
            # val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_max(self):
        if self.right is None: # if no more to the right, return value
            return self.data
        return self.right.find_max() # otherwise keep on going to the right

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
                # if nothing in the left
                # else:
                #     return None, is automatic
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val) # returns right subtree when on delete
        return self


def build_tree(elements):
    root = Tree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    t = build_tree(numbers)
    print(t.in_order_traversal())
    # print(t.search(20))

    t.delete(4)
    print(t.in_order_traversal())

