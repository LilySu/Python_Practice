class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_children(self, data):
        data.parent = self
        self.children.append(data)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spacing = ' ' * self.get_level()
        prefix = spacing + '|__' if self.parent else ''
        print(prefix + self.data)
        while len(self.children) > 0:
            for child in self.children:
                return child.print_tree()

def build_tree():
    branch = TreeNode("branch")
    branch.add_children(TreeNode("leaves"))

    trunk = TreeNode("trunk")
    trunk.add_children(branch)

    root = TreeNode("root")
    root.add_children(trunk)

    return root

if __name__ == '__main__':
    tree = build_tree()
    tree.print_tree()
    pass