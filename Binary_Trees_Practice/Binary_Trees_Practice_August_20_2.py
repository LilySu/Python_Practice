class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_children(self, item):
        item.parent = self
        self.children.append(item)

    def get_level(self):
        level = 0
        hasparent = self.parent
        while hasparent:
            hasparent = hasparent.parent
            level += 1
        return level

    def print_tree(self):
        print(self.data)
        if self.children:
            for child in self.children:
                return child.print_tree()

def build_tree():
    root = TreeNode("root")
    trunk = TreeNode("trunk")
    trunk.add_children(TreeNode("branch"))
    root.add_children(trunk)
    return root

if __name__ == "__main__":
    root = build_tree()
    root.print_tree()


