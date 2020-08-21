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
        print(spacing + self.data)
        if len(self.children) > 0:
            for child in self.children:
                return child.print_tree()

def build_tree():
    branch = TreeNode("branch")
    trunk = TreeNode("trunk")
    root = TreeNode("root")
    root.add_children(trunk)
    trunk.add_children(branch)
    return root

if __name__ == "__main__":
    b = build_tree()
    b.print_tree()
    pass