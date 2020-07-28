class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, data):
        data.parent = self
        self.children.append(data)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print(self):
        spaces = ' ' * self.get_level()
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print()

def build_tree():
    last = TreeNode("last")

    middle = TreeNode("middle")
    middle.add_child(TreeNode("front"))

    middle2 = TreeNode("middle2")
    middle2.add_child(TreeNode("front2"))

    last.add_child(middle)
    last.add_child(middle2)
    return last

if __name__ == '__main__':
    root = build_tree()
    root.print()
    pass