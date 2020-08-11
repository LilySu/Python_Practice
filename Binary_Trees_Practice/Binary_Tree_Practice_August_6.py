class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_children(self, child):
        child.parent = self
        self.children.append(child)

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

def buildtree():

    b = TreeNode("branch")
    b.add_children(TreeNode("leaf"))

    r = TreeNode("root")
    r.add_children(b)
    return r

if __name__ == '__main__':
    a = buildtree()
    a.printree()
    pass

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
            p = p.parent
            level += 1
        return p

    def printTree(self):
        spacing = self.get_level()
        prefix = spacing + '|__' if self.parent else '|'
        print(prefix + self.data)
        if len(self.children) > 0:
            for child in self.children:
                return child.printTree()