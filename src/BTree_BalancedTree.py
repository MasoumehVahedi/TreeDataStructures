"""
    BTree: is a self-balancing tree data structure that maintains sorted data and allows for efficient insertion, deletion, and search operations.
           It generalizes the concept of a binary search tree but allows each node to have more than two children.

    In a B-tree:
        1- t (the minimum degree or order) determines the minimum and maximum number of keys a node can hold.
        2- For a node in a B-tree of degree t:
              1- A node can hold at most 2t - 1 keys.
              2- A node must hold at least t - 1 keys (except the root, which can have fewer).

    Key Features of a B-tree:
        1- Multiple Keys Per Node: Each node can contain multiple keys. Instead of a single value like in a BST,
           a B-tree node can hold a range of values.
        2- Internal Nodes Hold Keys as Separators: In a B-tree, internal nodes contain keys that act as separators.
           Each key separates the child nodes into subranges.
        3- Range of Children Per Node: Each node has a minimum and maximum number of children. This is controlled by
           the tree's order, t, where each node must have between t and 2t - 1 keys.
        4- Height-Balanced: B-trees are always balanced, meaning that the paths from the root to any leaf node are of equal length.
        5- Efficient Disk Access: B-trees are optimized for reading/writing large blocks of data, making them ideal for databases and file systems.

"""


class BTreeNode:
    def __init__(self, is_leaf=None):
        self.is_leaf = is_leaf
        self.keys = []                   # holds the keys (values) in the node
        self.children = []               # references to the children (subtrees)

    def __repr__(self):
        return f"Keys: {self.keys}, Leaf: {self.is_leaf}"



class BTree:
    def __init__(self, min_degree):
        """
            BTree represents the entire B-tree structure.
            Params:
                - min_degree: Minimum degree of the B-tree.
        """
        self.root = BTreeNode(is_leaf=True)
        self.min_degree = min_degree             # Minimum degree of the B-tree
        self.MAX_KEYS = (2 * min_degree) - 1     # Maximum number of keys a node can have
        self.MIN_KEYS = min_degree - 1           # Minumum number of keys a node (except root) can have


    def insert(self, key):
        """
             If root is full (more than MAX_KEYS), it needs to be split:
               Step 1: Create a new root node (empty)
               Step 2: Make the current root a child of the new root
               Step 3: Split the old root (now a child of the new root)
               Step 4: Insert the new key into the new root
        """
        root = self.root      # local variable
        if len(root.keys) == self.MAX_KEYS:    # Root is full, needs to split
            new_root = BTreeNode(is_leaf=False)          # The new root will not be a leaf
            new_root.children.insert(0, root)
            self.splitNode(new_root, 0)
            self.insertNonFull(new_root, key)
            self.root = new_root  # Update root
        else:
            self.insertNonFull(root, key)    # If the root is not full, insert the key into the non-full root


    def insertNonFull(self, node, key):
        """
           Insert a key into a node that is not full.
           Params:
             - node: The node in which to insert the key (or recurse into)
             - key: The key-value pair to be inserted into BTree.

           - index: This tracks the position inside the keys list of the current node, starting from the rightmost
                  key and moving left to find the correct position for the new key.
        """
        index = len(node.keys) - 1    # Start at the rightmost key

        if node.is_leaf:
            # If the node is a leaf, insert the key directly here
            node.keys.append((None, None))
            # goal of this loop: to maintain the sorted order
            while index >= 0 and key[0] < node.keys[index][0]:
                node.keys[index + 1] = node.keys[index]       # Shift the larger keys to the right
                index -= 1
            node.keys[index + 1] = key     # Insert the new key at the correct position
        else:
            # If the node is an internal node, we need to recurse into the correct child
            while index >= 0 and key[0] < node.keys[index][0]:
                index -= 1
            index += 1

            # Check if the child is full
            if len(node.children[index].keys) == self.MAX_KEYS:
                self.splitNode(node, index)
                # After splitting, check if the key should go into the new child
                if key[0] > node.keys[index][0]:
                    index += 1

            # Recur into the appropriate child to insert the key
            self.insertNonFull(node.children[index], key)


    def splitNode(self, parent_node, node_index):
        """
            Params:
            1- parent_node: This is the parent of the full child that is being split.
                                The middle key from the full child will be promoted to this parent.
            2- node_index: This is the index in the parent where the full child is located.

        - full_node: The child node that is full and needs to be split.
        - new_node: The new node that will hold the right half of the keys from the full child.
        """
        full_node = parent_node.children[node_index]
        new_node = BTreeNode(full_node.is_leaf)                    # Create a new node
        parent_node.children.insert(node_index + 1, new_node)      # Insert the new child node
        # Move the middle key of the full child up to the parent node
        parent_node.keys.insert(node_index, full_node.keys[self.min_degree - 1])
        # Split the keys of the full child into two parts
        new_node.keys = full_node.keys[self.min_degree: self.MAX_KEYS]   # The new child gets the right half (keys greater than the middle key)
        full_node.keys = full_node.keys[0: self.MIN_KEYS]                # The full child keeps the left half (keys less than the middle key)

        if not full_node.is_leaf:
            new_node.children = full_node.children[self.min_degree: (2 * self.min_degree)]  # Right half of the children
            full_node.children = full_node.children[0: self.MIN_KEYS]   # Left half of the children


    def search(self, search_key, node=None):
        """
            Search for a key in the B-tree.
            Params:
              - search_key: The key being searched for in the B-tree.
              - current_node: The node where the search starts. If None, it starts from the root.
            return:
              - Tuple (node, index) where the key is found, or None if not found.
        """
        if node is not None:
            key_index = 0
            while key_index < len(node.keys) and search_key > node.keys[key_index][0]:
                key_index += 1
            if key_index < len(node.keys) and search_key == node.keys[key_index][0]:
                return node, key_index
            elif node.is_leaf:
                return None
            else:
                return self.search(search_key, node.children[key_index])
        else:
            # If no node is provided, start the search from the root
            return self.search(search_key, self.root)


    def printBTree(self, node, level=0):
        print("Level", level, ":", len(node.keys), "keys", end=" -> ")
        for key in node.keys:
            print(key, end=" ")
        print()
        level += 1
        if len(node.children) > 0:
            for child in node.children:
                self.printBTree(child, level)

