# def print_tree(self):
#     print(self.data)
#     if self.children:
#         for child in self.children:
#             child.print_tree()
#
# def add_children(self, child):
#     child.parent = self
#     self.children.append(child)

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        counter = 0
        p = self.parent
        while p:
            counter += 1
            p = p.parent
        return counter

    def print_tree(self):
        indent = ' ' * self.get_level()
        prefix = indent + '|__' if self.parent else '|'
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_children(self, data):
        data.parent = self
        self.children.append(data)

def build_tree():
    tree = TreeNode('tree')

    branch = TreeNode('branch')

    trunk = TreeNode('trunk')
    trunk.add_children(branch)

    root = TreeNode('root')
    root.add_children(trunk)

    tree.add_children(root)

    return tree

if __name__ == '__main__':
    root = build_tree()
    root.print_tree()