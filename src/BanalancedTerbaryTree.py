"""
   Ternary Tree:
   A Ternary Tree is a type of tree data structure where each node can have up to three child nodes.

   In a ternary tree:
   - Each node has three possible children: a left child, a middle child, and a right child.
   - The nodes are connected by edges that represent the parent-child relationships.
"""




class Interval:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __repr__(self):
        return f"[{self.low}, {self.high}]"


class Node:
    def __init__(self, interval=None, intervals=None):
        self.interval = interval  # Single interval for non-leaf nodes
        self.intervals = intervals if intervals is not None else []      # List of intervals for leaf nodes
        self.left = None
        self.right = None
        self.overlapped = None

    def __repr__(self):
        if self.intervals:
            return f"Leaf: {self.intervals}"
        return f"Node: [{self.interval.low}, {self.interval.high}]"


class Tree:
    def __init__(self, max_entries):
        self.max_entries = max_entries
        self.root = None


    def buildBalancedTree(self, intervals):
        intervals.sort(key=lambda interval: interval.low)
        self.root = self._buildTree(intervals, 0, len(intervals) - 1)


    def _buildTree(self, intervals, start, end):
        if start > end:
            return

        if len(intervals) <= self.max_entries:
            node = Node()
            node.intervals = intervals
            return node

        mid = (start + end) // 2
        node = Node(intervals[mid])

        left_intervals, overlapped_intervals, right_intervals = self.splitNode(intervals, node)
        #print(f"intervals = {left_intervals}, {overlapped_intervals}, {right_intervals}")

        if len(left_intervals) > 0:
            node.left = self._buildTree(left_intervals, 0, len(left_intervals) - 1)
        if len(overlapped_intervals) > 0:
            node.overlapped = self._buildTree(overlapped_intervals, 0, len(overlapped_intervals) - 1)
        if len(right_intervals) > 0:
            node.right = self._buildTree(right_intervals, 0, len(right_intervals) - 1)

        return node


    def splitNode(self, intervals, node):
        left, overlapped, right = [], [], []
        for interval in intervals:
            if interval.high < node.interval.low:
                left.append(interval)
            elif interval.low > node.interval.high:
                right.append(interval)
            else:
                overlapped.append(interval)   # Only add to overlapped

        return left, overlapped, right


    def search(self, query):
        pass


    def printTree(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root

        if node.intervals:  # If the node is a leaf node with multiple intervals
            print(' ' * (level * 4) + f"{prefix}Leaf: {node.intervals}")
        else:  # If the node is a non-leaf node with a single interval
            print(' ' * (level * 4) + f"{prefix}[{node.interval.low}, {node.interval.high}]")

        # Traverse the right subtree
        if node.right is not None:
            self.printTree(node.right, level + 1, "R--- ")
        # Traverse the left subtree
        if node.left is not None:
            self.printTree(node.left, level + 1, "L--- ")
        # Traverse the overlapped subtree
        if node.overlapped is not None:
            self.printTree(node.overlapped, level + 1, "O--- ")



"""if __name__ == "__main__":
    intervals = [Interval(12, 15), Interval(1, 5), Interval(20, 30), Interval(9, 11),
                 Interval(6, 8), Interval(18, 22), Interval(16, 21), Interval(25, 32)]

    tree = Tree(max_entries=3)
    tree.buildBalancedTree(intervals)
    tree.printTree()"""


