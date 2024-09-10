"""
    Binary Search Tree:
    A binary tree is a tree data structure where each node has at most two children, often referred to as the left child and the right child.

    The key difference between building a balanced and an unbalanced tree is the order of the nodes:

    1- Unbalanced Tree:
       1- We insert nodes one by one in the order they are provided. This doesn't consider balancing the tree.
       2- We don’t use the middle value because we’re not trying to keep the tree balanced.

    2- Balanced Tree:
        1- We first collect all nodes in a sorted array and then use the middle value to ensure that the tree is balanced.
        2- Using the middle value allows us to split the array evenly and create a balanced structure.

"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class UnbalancedBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = TreeNode(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left == None:
                current_node.left = TreeNode(data)
            else:
                self._insert(data, current_node.left)
        else:
            if current_node.right == None:
                current_node.right = TreeNode(data)
            else:
                self._insert(data, current_node.right)

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level+1)
            print(' ' * 4 * level + '->', node.data)
            self.printTree(node.left, level+1)



class BalancedBinaryTree:
    """ Construct a balanced BST in O(n) time with minimum possible height. These are efficient solution:

        1- Traverse given BST in inorder and store result in an array. This step takes O(n) time.
           Note that this array would be sorted as InOrder traversal (left-root-right) of BST always produces sorted sequence.
        2- Build a balanced BST from the above created sorted array using the recursive approach.
           This step also takes O(n) time as we traverse every element exactly once and processing an element takes O(1) time.
    """
    def __init__(self):
        self.root = None

    def storeBSTNodes(self, node, nodes):
        """ Traverse the BST in inorder and store the nodes in a list.
            - nodes is simply a list (nodes = []) that is used to store all the nodes from
                  the binary search tree (BST) when performing an in-order traversal.
        """
        if node is None:
            return

        # Inorder traversal (left-root-right)
        self.storeBSTNodes(node.left, nodes)
        nodes.append(node)   # Add the current node to the list
        self.storeBSTNodes(node.right, nodes)

    def buildBalancedTree(self, nodes, start, end):
        """ Recursive function to build a balanced BST from sorted nodes. """
        if start > end:
            return

        mid = (start + end) // 2
        node = nodes[mid]

        # Recursively build the left and right subtrees
        node.left = self.buildBalancedTree(nodes, start, mid - 1)
        node.right = self.buildBalancedTree(nodes, mid + 1, end)

        return node

    def _buildBalancedTree(self, root):
        """ Convert the unbalanced BST to a balanced one. """
        nodes = []
        self.storeBSTNodes(root, nodes)   # Store the nodes in a sorted order (inorder traversal)
        # Rebuild the balanced tree using the sorted list of nodes
        return self.buildBalancedTree(nodes, start=0, end=len(nodes)-1)


    def preOrderTraversal(self, node):
        """ Preorder traversal to print the tree structure (root-left-right). """
        if node is None:
            return
        print(f"Root={node.data} -> ", end=" ")
        self.preOrderTraversal(node.left)
        self.preOrderTraversal(node.right)

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level+1)
            print(' ' * 4 * level + '->', node.data)
            self.printTree(node.left, level+1)


