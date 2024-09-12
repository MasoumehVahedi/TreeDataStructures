"""
    How to balance an Interval Tree?
    After inserting intervals, the tree might be unbalanced (similar to a regular binary search tree).
    There are two approaches:

        (1) AVL Tree (dynamic balancing with rotations).
        (2) Rebuild the Tree (static balancing by collecting and re-inserting).




"""

from TreeDataStructure.src.IntervalTree import Node



class BalancedIntervalTree:
    def __init__(self):
        self.root = None

    def insert(self, interval):
        if self.root is None:
            self.root = Node(interval)
        else:
            self._insert(self.root, interval)


    def _insert(self, node, interval):
        if node is None:
            return Node(interval)

        if interval.low < node.interval.low:
            node.left = self._insert(node.left, interval)
        else:
            node.right = self._insert(node.right, interval)

        # Update max of node
        node.max = max(node.max, interval.high)

        return node


    def inOrderTraversal(self, node, intervals):
        """ Collect Intervals (Inorder Traversal):
            Param:
            - intervals is simply a list (nodes = []) that is used to store all the nodes from
                  the binary search tree (BST) when performing an in-order traversal.
        """
        if node is None:
            return None

        self.inOrderTraversal(node.left, intervals)
        intervals.append(node.interval)
        self.inOrderTraversal(node.right, intervals)

    def buildBalancedTree(self, intervals, start, end):

        if start > end:
            return

        mid = (start + end) // 2
        node = Node(intervals[mid])

        # Recursively build the left and right subtrees
        node.left = self.buildBalancedTree(intervals, start, mid - 1)
        node.right = self.buildBalancedTree(intervals, mid + 1, end)

        # Correct the max value based on the left and right subtrees
        node.max = node.interval.high
        if node.left:
            node.max = max(node.max, node.left.max)
        if node.right:
            node.max = max(node.max, node.right.max)

        return node

    def rebuildTree(self, node):
        """ Rebuild the tree from collected intervals. """
        intervals = []
        self.inOrderTraversal(node, intervals)
        return self.buildBalancedTree(intervals, start=0, end=len(intervals) - 1)


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

    def printTree(self, node=None, level=0, prefix="Root: "):
        """ Print the tree in a hierarchical way to visualize the structure clearly. """
        if node is None:
            node = self.root  # Start from the root

        # Print the current node with indentation corresponding to its level
        print(' ' * (level * 4) + f"{prefix}[{node.interval.low}, {node.interval.high}] (Max: {node.max})")

        # Traverse the right subtree
        if node.right is not None:
            self.printTree(node.right, level + 1, "R--- ")

        # Traverse the left subtree
        if node.left is not None:
            self.printTree(node.left, level + 1, "L--- ")





