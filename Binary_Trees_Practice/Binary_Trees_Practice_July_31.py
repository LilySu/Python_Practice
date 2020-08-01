class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        pointer = self.parent
        while pointer:
            pointer = pointer.next
            level += 1
        return level

    def print_tree(self):
        print(self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()

    def add_children(self, child):
        child.parent = self
        self.children.append(child)

def build_tree():
    c = TreeNode("child")
    c.add_children(TreeNode("mini"))
    m = TreeNode("middle")
    m.add_children(c)
    r = TreeNode("root")
    r.add_children(m)
    return r

if __name__ == '__main__':
    a = build_tree()
    a.print_tree()
    pass


def add_children(self, data):
    data.parent = self
    self.children.append(data)


def add_children(self, data):
    data.parent = self
    self.children.append(data)

def add_children(self, data):
    data.parent = self
    self.children.append(data)