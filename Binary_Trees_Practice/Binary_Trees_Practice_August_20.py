class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, data):
        data.parent = self
        self.children.append(data)

    def get_level(self):
        p = self.parent
        level = 0
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        indent = self.get_level() * ' '
        print(indent + self.data)
        if self.children:
            for child in self.children:
                return child.print_tree()

def build_tree():
    a = TreeNode("a")
    b = TreeNode("b")
    c = TreeNode("c")
    a.add_child(b)
    b.add_child(c)
    c.add_child(TreeNode("e"))
    return a

if __name__ == "__main__":
    a = build_tree()
    a.print_tree()
    pass