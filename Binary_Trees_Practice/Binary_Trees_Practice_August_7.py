class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_children(self, data):
        self.parent = self
        self.children.append(data)

    def printree(self):
        print(self.data)
        if len(self.children) > 0:
            for child in self.children:
                return child.printree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

def build_tree():
    c = TreeNode('c')
    c.add_children(TreeNode('d'))
    b = TreeNode('b')
    b.add_children(c)
    a = TreeNode('a')
    a.add_children(b)
    return a

if __name__ == '__main__':
    r = build_tree()
    r.printree()
    pass