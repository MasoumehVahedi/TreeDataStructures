from TreeDataStructure.src.BinaryTree import UnbalancedBinaryTree
from TreeDataStructure.src.BinaryTree import BalancedBinaryTree


def main():
    # ----------------------------------------------------------------------- #
    #                   Unbalanced Binary Search Tree
    # ----------------------------------------------------------------------- #
    unbalanced_tree = UnbalancedBinaryTree()
    elemnts = [1, 2, 3, 4, 5]
    # inserting the elements in increasing order
    for el in elemnts:
        unbalanced_tree.insert(el)

    print("Unbalanced Binary Tree (Right-Skewed):")
    # The tree is a right-skewed (unbalanced binary search tree)
    unbalanced_tree.printTree(unbalanced_tree.root)

    # ----------------------------------------------------------------------- #
    #                   Balanced Binary Search Tree
    # ----------------------------------------------------------------------- #
    balanced_tree = BalancedBinaryTree()
    # Build the balanced tree from the unbalanced tree's root
    balanced_root = balanced_tree._buildBalancedTree(unbalanced_tree.root)
    print("\nBalancing the tree:")
    balanced_tree.printTree(balanced_root)

    print("\nBalanced Binary Tree (Preorder Traversal):")
    balanced_tree.preOrderTraversal(balanced_root)   # answer: 3 1 2 4 5


if __name__ == "__main__":
    main()