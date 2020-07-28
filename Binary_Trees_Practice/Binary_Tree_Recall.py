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
        indent = ' ' * self.get_level()
        spaces = indent + '|__' if self.parent else ''
        print(spaces + self.data)
        if len(self.children) > 0:
            for child in self.children:
                return child.print_tree()

def build_tree():
    root = TreeNode("root")

    trunk = TreeNode("trunk")
    branch = TreeNode("branch")
    leaf = TreeNode("leaf")
    leaf.add_child(TreeNode("vein"))
    branch.add_child(leaf)
    trunk.add_child(branch)
    root.add_child(trunk)

    return root

if __name__ == '__main__':
    root = build_tree()
    root.print_tree()
    pass