class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self # child is instance of treenode class, set parent property as self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level()
        prefix = spaces + '|__'
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    root.add_child(laptop)
    return root

if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
    print(root.get_level())
    pass
