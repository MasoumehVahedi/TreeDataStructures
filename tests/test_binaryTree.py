import os
import sys

sys.path.append('../')

import unittest
from src.BinaryTree import TreeNode, UnbalancedBinaryTree, BalancedBinaryTree


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.elements = [3, 1, 4, 2, 5]  # Unsorted elements
        self.unbalanced_tree = UnbalancedBinaryTree()
        self.balanced_tree = BalancedBinaryTree()

    def test_root_init(self):
        root = self.unbalanced_tree.insert(1)
        self.assertEqual(root.data, 1)
        self.assertEqual(root.left, None)
        self.assertEqual(root.right, None)


    def test_build_balanced_tree(self):
        for el in self.elements:
            self.unbalanced_tree.insert(el)

        # Rebuild tree to balanced one
        balanced_root = self.balanced_tree._buildBalancedTree(self.unbalanced_tree.root)

        # Perform in_order traversal
        in_order_result = []
        self.balanced_tree.storeBSTNodes(balanced_root, in_order_result)
        result_data = [node.data for node in in_order_result]

        self.assertEqual(result_data, sorted(self.elements))


    def test_pre_order_traversal(self):
        for el in self.elements:
            self.unbalanced_tree.insert(el)

        # Rebuild tree to balanced one
        balanced_root = self.balanced_tree._buildBalancedTree(self.unbalanced_tree.root)

        pre_order_result = []
        self.balanced_tree.preOrderTraversal(balanced_root, pre_order_result)

        expected_result = [3, 1, 2, 4, 5]
        self.assertEqual(pre_order_result, expected_result)



if __name__ == "__main__":
    unittest.main()


