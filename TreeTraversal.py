"""
    Traversal Strategy:
    1- BFS (Breadth-First Search) (also known as Level-Order Traversal): Processes the tree level by level using a queue.
    2- DFS (Depth-First Search) (Inorder, Preorder, and Postorder are DFS) : Goes deep into each branch before moving to
       the next branch, using recursion or a stack.


    DFS (Depth-First Search) (Inorder, Preorder, and Postorder are DFS):
    1- DFS explores as deep as possible along one branch before backtracking and exploring other branches.
    2- It dives into a subtree first, and only after completing that subtree, it moves to the next subtree.
    3- Uses recursion or a stack to go deep into one subtree before moving to the next.
    4- Less memory-intensive for deep trees because it only needs to store nodes in the current path.
    5- Inorder traversal, specifically, is useful in binary search trees (BSTs) because it visits nodes in sorted order.

    When to Use DFS:
    1- When you need to explore an entire subtree before moving to the next one.
    2- When you're working with binary trees (e.g., Inorder traversal gives nodes in sorted order for Binary Search Trees).
    3- When you need to process nodes in a specific order, like visiting the root first (Preorder) or last (Postorder).


    What is Level-Order Traversal?
    - In level-order traversal, you visit all the nodes at one level before moving to the next level.
      This means you first visit the root node, then all the nodes at depth 1, followed by all the nodes at depth 2, and so on.
    - It’s like reading a book from left to right across each "line" or "level" of the tree before moving to the next line.
    - Queue is essential for level-order traversal because it follows a first-in, first-out (FIFO) principle, which is necessary
      for processing nodes level by level.
      You start by adding the root node to the queue. Then, you repeatedly:
          1- Remove the node at the front of the queue.
          2- Process it (usually by printing or storing its value).
          3- Add its children to the end of the queue.
      This ensures that you process all nodes at the current level before moving to the next level, as the children of each node will
      only be added after their parent has been processed.


    For example, in R-tree implementation, we use BFS, not DFS.
    Why BFS (and not DFS) in R-Trees?
    1- BFS (Level-Order Traversal): R-trees prioritize exploring nodes level by level, meaning you check all the child nodes at a
                                   given depth (bounding boxes that overlap with the query) before going to the next depth.
                                   This ensures that you can prune entire subtrees early, improving efficiency.
    2- Queue in BFS: A queue is used to keep track of the nodes (bounding boxes) to be checked. As you check each node,
                 if its bounding box overlaps with your query, you add its children to the queue for further exploration.
                 This continues until all relevant nodes are processed.
    3- DFS (Depth-First Search): In contrast, DFS would explore one branch of the tree (one child/subtree) as deeply as possible
                                 before backtracking. This isn't as efficient for spatial queries because it could waste time diving
                                 deep into irrelevant regions that don’t overlap with the query.

"""

from collections import deque


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addLeftChild(self, child):
        self.left = BinaryTreeNode(child)

    def addRightChild(self, child):
        self.right = BinaryTreeNode(child)

    def __repr__(self):
        return f"TreeNode(Data = {self.data})"



class DFS:
    """ DFS (Depth-First Search) (Inorder, Preorder, and Postorder are DFS):
        1- DFS explores as deep as possible along one branch before backtracking and exploring other branches.
        2- It dives into a subtree first, and only after completing that subtree, it moves to the next subtree.
        3- Uses recursion or an explicit stack to explore deep paths in the tree.
    """

    def InOrderTraversal(self, root):
        """ In-order Traversal: Recursively visit:
            1- First, visit all the nodes in the left sub-tree
            2- Then the root node
            3- Visit all the nodes in the right sub-tree
        """
        if root is None:
            return None

        if root:
            self.InOrderTraversal(root.left)          # Traverse left
            print(f"Node={root.data} -> ", end=" ")   # Traverse root
            self.InOrderTraversal(root.right)         # Traverse right


    def preOrderTraversal(self, root):
        """ Pre-order Traversal:
            1- Visit root node
            2- Visit all the nodes in the left sub-tree
            3- Visit all the nodes in the right sub-tree
        """
        if root is None:
            return None

        if root:
            print(f"Root={root.data} -> ", end=" ")   # Traverse root
            self.preOrderTraversal(root.left)         # Traverse left
            self.preOrderTraversal(root.right)        # Traverse right

    def postOrderTraversal(self, root):
        """ Post-order Traversal:
            1- Visit all the nodes in the left sub-tree
            2- Visit all the nodes in the right sub-tree
            3- Visit the root node.
        """
        if root is None:
            return

        if root:
            self.postOrderTraversal(root.left)        # Traverse left
            self.postOrderTraversal(root.right)       # Traverse right
            print(f"Root={root.data} -> ", end=" ")   # Traverse root



class BFS:
    """ BFS (Breadth-First Search) (also known as Level-Order Traversal):
        1- BFS explores all nodes at the current level before moving on to nodes at the next level.
        2- It "moves across" the tree level by level, processing the tree layer by layer.
        3- Uses a queue to keep track of nodes at each level
    """

    def levelOrderTraversal(self, root):
        if root is None:
            return None
        queue = deque([root])
        while queue:
            # Pop the node at the front of the queue
            current_node = queue.popleft()
            print(current_node.data)

            # Add the left and right children if they exist
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)








