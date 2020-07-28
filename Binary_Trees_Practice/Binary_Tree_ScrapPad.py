class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 2
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()

def build_tree():
    root = TreeNode("Bottom")

    branch1 = TreeNode("branch1")
    branch1.add_child(TreeNode("leaf1"))

    branch2 = TreeNode("branch2")
    branch2.add_child(TreeNode("leaf2"))

    root.add_child((branch1))
    root.add_child((branch2))
    return root

if __name__ == '__main__':
    root = build_tree()
    root.print_tree()
    pass
