import numpy as np
import matplotlib.pyplot as plt

#################### Binary Search Tree ####################

class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            # Add data in the left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)
        else:
            # Add data in the right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)

    def searchTree(self, value):
        if value == self.data:
            return True
        if value < self.data:
            # Search left subtree
            if self.left:
                return self.left.searchTree(value)
            else:
                return False
        if value > self.data:
            # Search right subtree
            if self.right:
                return self.right.searchTree(value)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        # 1- Visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # 2- Visit base node
        elements.append(self.data)
        # 3- Visit right tree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        """ The root is BEFORE left and right subtree """
        elements = []
        # 1- Visit the base node
        elements.append(self.data)

        # 2- visit left subtree
        if self.left:
            elements += self.left.pre_order_traversal()

        # 3- Visit right subtree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        """ The root is AFTER left and right subtree """
        elements = []
        # 1- visit left subtree
        if self.left:
            elements += self.left.post_order_traversal()

        # 2- visit right subtree
        if self.right:
            elements += self.right.post_order_traversal()

        # 3- visit base node
        elements.append(self.data)

        return elements


def buildTree(data):
    root = BST(data[0])
    for i in range(1, len(data)):
        root.add_child(data[i])
    return root



if __name__ == "__main__":
    elements = [12, 1, 50, 32, 5, 10, 9, 2, 38, 25, 22, 45, 8]
    tree = buildTree(elements)
    # 1- Build In-Order Binary Search Tree
    print(tree.in_order_traversal())   # It returns a sorted array
    print(tree.searchTree(20))   # False
    print(tree.searchTree(50))   # True

    # 2- Build Pre-Order Binary Search Tree
    print(tree.pre_order_traversal())
    # 3- Build Post-Order Binary Search Tree
    print(tree.post_order_traversal())



