import os
import sys

sys.path.append('../')

import unittest
from src.IntervalTree_balanced import BalancedIntervalTree


class TestIntervalTree(unittest.TestCase):
    def setUp(self):
        self.elements = [1, 2, 3, 4, 5]
        self.idx = BalancedIntervalTree()
        for el in self.elements:
            self.idx.insert(el)

    def test_BST(self):
        root = self.idx.root
        self.assertEqual(len(root.data), 5)




if __name__ == "__main__":
    unittest.main()


