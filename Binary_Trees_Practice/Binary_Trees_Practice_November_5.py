class BuildTree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, data):
        data.parent = self
        self.children.append(data)

    def get_level(self):
        level = 0
        pointer = self.parent
        while pointer:
            pointer = pointer.parent
            level += 1
        return level

    def print_tree(self):
        indent = self.get_level() * ' '
        prefix = indent + '|__' if self.parent else ''
        print(prefix + self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()

def build_tree():
    r = BuildTree("rob")
    s = BuildTree("sam")
    t = BuildTree("trey")
    s.add_child(t)
    r.add_child(s)

    return r

if __name__ == "__main__":
    a = build_tree()
    a.print_tree()