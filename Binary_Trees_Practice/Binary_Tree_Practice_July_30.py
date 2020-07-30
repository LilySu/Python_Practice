class Binary_Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        counter = 0
        p = self.parent
        while p:
            p = p.parent
            counter += 1
        return counter

    def print_tree(self):
        print(self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_children(self, child):
        child.parent = self
        self.children.append(child)

def build_tree():
    r = Binary_Tree("root")
    r.add_children(Binary_Tree("branch"))
    return r


if __name__ == '__main__':
    t = build_tree()
    t.print_tree()