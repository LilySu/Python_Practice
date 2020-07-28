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
        indent = ' ' * self.get_level()
        spacing = indent + '|__' if self.parent else ''
        print(spacing + self.data)
        while len(self.children) > 0:
            for child in self.children:
                return child.print_tree()

def build_tree():
    s = TreeNode("small")
    s.add_children(TreeNode("tiny"))
    m = TreeNode("medium")
    m.add_children(s)
    l = TreeNode("large")
    l.add_children(m)
    return l

if __name__ == '__main__':
    tree = build_tree()
    tree.print_tree()
    pass