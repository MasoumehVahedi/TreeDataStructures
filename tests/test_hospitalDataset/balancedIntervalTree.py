

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


    def isOverlapping(self, root, search_interval, results):
        """ Overlapping Interval Search:
            This function checks if an interval overlaps with any interval in the tree.
        """
        if root is None:
            return

        # If the root's interval overlaps with the search_interval
        if root.interval.low <= search_interval.high and search_interval.low <= root.interval.high:
            results.append(root.interval)

        # If the left child's max is greater than or equal to the search_interval's low, search in the left subtree
        if root.left is not None and root.left.max >= search_interval.low:
            self.isOverlapping(root.left, search_interval, results)

        # Otherwise, check the right subtree
        self.isOverlapping(root.right, search_interval, results)


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

