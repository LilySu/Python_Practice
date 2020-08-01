class TreeNode:
    # each element will be an instance of tree node class
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None # store parent of node, tree node is an individual node within the tree

    def add_child(self, child): # add child node into tree
        child.parent = self # child parent property set as self
        self.children.append(child) # the self will be a parent of the child

    def get_level(self):
        level = 0
        p = self.parent
        while p: # keep on going through parent and increase level
            level += 1
            p = p.parent
        return level

    def print_tree(self):# print data element in children, since tree is recursive, on child node, we again call function
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|--' if self.parent else ''
        print(prefix+ self.data)
        # print(self.data)
        if len(self.children) > 0:
            for child in self.children:
                # print(child.data) # prints the 3 children of electronics
                child.print_tree()

def build_product_tree():
    root = TreeNode("Electronics") # stored in self.data of root node

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac")) # add_child child becomes instance of tree node
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    # root.print_tree()

    # print(tv.get_level())

    return root

if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
    # print(root.get_level())
    pass