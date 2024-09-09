from simpleTree import Tree, TreeNode
from TreeTraversal import BinaryTreeNode, DFS, BFS


def buildSimpleTree():
    # Initialize tree with root
    tree = Tree("A")
    # Create children nodes
    child1 = TreeNode("B")
    child2 = TreeNode("C")
    child3 = TreeNode("D")
    child4 = TreeNode("E")
    child5 = TreeNode("F")
    # Add children to the root
    tree.addChildToRoot(child1)
    tree.addChildToRoot(child2)
    tree.addChildToRoot(child3)
    tree.addChildToRoot(child4)
    tree.addChildToRoot(child5)

    print("Tree structure = ", tree)
    print("Root's children = ", tree.root.children)


def buildBinaryTree():
    """
    We want to create this binary tree:
             1
           /   \
         2       3
        / \     / \
       4   5   6   7
      / \       / \
     8   9     10  11

    """
    root = BinaryTreeNode(1)   # root node
    # Level 1
    root.addLeftChild(2)
    root.addRightChild(3)
    #print("Root node:", root)
    #print("Left child of root:", root.left)
    #print("Right child of root:", root.right)

    # Level 2
    root.left.addLeftChild(4)
    root.left.addRightChild(5)
    root.right.addLeftChild(6)
    root.right.addRightChild(7)
    #print("Left child of left child of root:", root.left.left)
    #print("Right child of left child of root:", root.left.right)
    #print("Left child of right child of root:", root.right.left)
    #print("Right child of right child of root:", root.right.right)

    # Level 3
    root.left.left.addLeftChild(8)
    root.left.left.addRightChild(9)
    root.right.left.addLeftChild(10)
    root.right.left.addRightChild(11)
    #print("Left left child of left child of root:", root.left.left.left)
    #print("Left right child of left child of root:", root.left.left.right)
    #print("Right left child of right child of root:", root.right.left.left)
    #print("Right right child of right child of root:", root.right.left.right)


    # ----------------------------------------------------------------------- #
    #                   Tree Traversal: DFS (Depth-First Search)
    # ----------------------------------------------------------------------- #
    search_dfs = DFS()

    print("Inorder traversal ")
    search_dfs.InOrderTraversal(root)

    print("\nPreorder traversal ")
    search_dfs.preOrderTraversal(root)

    print("\nPostorder traversal ")
    search_dfs.postOrderTraversal(root)

    # ----------------------------------------------------------------------- #
    #                   Tree Traversal: BFS (Breadth-First Search)
    # ----------------------------------------------------------------------- #
    search_bfs = BFS()
    print("Level-Order Traversal")
    search_bfs.levelOrderTraversal(root)


def main():
    buildSimpleTree()
    buildBinaryTree()


if __name__ == "__main__":
    main()