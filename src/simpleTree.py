
class TreeNode:
    def __init__(self, entries):
        self.entries = entries
        self.children = []

    def addChild(self, child):
        """ Add a child node to the current node. """
        self.children.append(child)

    def __repr__(self):
        return f"TreeNode(Entries = {self.entries})"



class Tree:
    def __init__(self, root_data=None):
        # Initialize a tree with a root node
        if root_data is not None:
            self.root = TreeNode(root_data)
        else:
            self.root = None

    def addChildToRoot(self, child_node):
        """ Add a child into the root node of the tree. """
        if self.root == None:
            raise ValueError("Root is not set.")
        self.root.addChild(child_node)

    def __repr__(self):
        return f"Tree(root={self.root})"