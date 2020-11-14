class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, data):
        data.parent = self
        self.children.append(data)

    def get_level(self):
        p = self.parent
        counter = 0
        while p:
            counter += 1
            p = p.parent
        return counter

    def print_tree(self):
        indent = self.get_level() * " "
        prefix = indent + "|__" if self.parent else ""
        print(prefix + self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()

def build_tree():
    b = BinaryTree("branch")
    t = BinaryTree("tree")
    r = BinaryTree("root")
    d = BinaryTree("dirt")
    d.add_child(r)
    r.add_child(t)
    t.add_child(b)
    return d

if __name__ == "__main__":
    tree = build_tree()
    tree.print_tree()


