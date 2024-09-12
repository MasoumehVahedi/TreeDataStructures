"""
    Interval Tree:
    An Interval Tree is a type of binary search tree (BST) where each node stores an interval [low, high] and a max value
    that represents the maximum high value in the subtree rooted at that node.

    Interval Tree Components:
        1- Node: Stores the interval, a max value, and references to the left and right children.
        2- Insert: Inserts intervals into the tree.
        3- Search: Searches for overlapping intervals.
"""


class Interval:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __str__(self):
        return f"[{self.low}, {self.high}]"


class Node:
    def __init__(self, interval):
        self.interval = interval
        self.max = interval.high    # The maximum high value in this subtree
        self.left = None
        self.right = None

    def __str__(self):
        return f"Interval: {self.interval}, Max: {self.max}"



class UnbalancedIntervalTree:
    def __init__(self):
        self.root = None

    def insert(self, interval):
        if self.root is None:
            self.root = Node(interval)
        else:
            self._insert(self.root, interval)

    def _insert(self, current_node, interval):
        if current_node is None:
            return Node(interval)

        if interval.low < current_node.interval.low:
            current_node.left = self._insert(current_node.left, interval)
        else:
            current_node.right = self._insert(current_node.right, interval)

        # Update the max value for this node
        current_node.max = max(current_node.max, interval.high)

        return current_node


    def inOrder(self, node):
        """ Inorder Traversal (left, root, right). """
        if node is None:
            return None

        self.inOrder(node.left)
        print(f"Node= {node.interval} -> Max= {node.max}")
        self.inOrder(node.right)


    def isOverlapping(self, root, search_interval):
        """ Overlapping Interval Search:
            This function checks if an interval overlaps with any interval in the tree.
        """
        if root is None:
            return None

        # if search interval overlaps with root's interval:
        # Loginc ->  low_root <= search_key high   and   search_key low <= high_root
        if root.interval.low <= search_interval.high and search_interval.low <= root.interval.high:
            return root.interval

        # if the max value of left subtree is greater than or equal to the low value of the query interval:
        # Logic -> max(left subtree) >= search_key low
        elif root.left is not None and root.left.max >= search_interval.low:
            return self.isOverlapping(root.left, search_interval)
        else:
            # Otherwise, search the right subtree
            return self.isOverlapping(root.right, search_interval)


    def printTree(self, node, level=0):
        """ Print the tree in a structured way, showing levels. """
        if node is None:
            node = self.root  # Start from the root

        if node.right is not None:
            self.printTree(node.right, level + 1)

        # Print the current node with indentation corresponding to its level
        print(' ' * 4 * level + f"-> {node.interval} (Max: {node.max})")

        if node.left is not None:
            self.printTree(node.left, level + 1)




