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
        spaces = '  ' * self.get_level() * 2
        prefix = spaces + '|--' if self.parent else ''
        print(prefix + self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()

def build_tree():
    top = TreeNode("top")

    middle1 = TreeNode("middle1")
    middle1.add_children(TreeNode("children1"))
    middle1.add_children(TreeNode("children12"))

    middle2 = TreeNode("middle2")
    middle3 = TreeNode("middle3")

    top.add_children(middle1)
    top.add_children(middle2)
    top.add_children(middle3)

    return top

if __name__ == "__main__":
    top = build_tree()
    top.print_tree()
    pass