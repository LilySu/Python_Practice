class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_children(self, data):
        data.parent = self
        self.children.append(data)

    def get_level(self):
        l = 0
        p = self.parent
        while p:
            l += 1
            p = p.parent
        return l

    def print_tree(self):
        spaces = ' ' * self.get_level()
        prefix = spaces + '|__' if self.parent else '|'
        print(prefix + self.data)
        while len(self.children) > 0:
            for child in self.children:
                return child.print_tree()

def build_tree():
    l = TreeNode("leaves")
    l.add_children(TreeNode("stems"))
    b = TreeNode("branches")
    b. add_children(l)
    t = TreeNode("trunk")
    t.add_children(b)
    return t

if __name__ == '__main__':
    t = build_tree()
    t.print_tree()


