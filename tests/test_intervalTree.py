import sys
sys.path.append('../')


import unittest
from src.IntervalTree_balanced import BalancedIntervalTree
from src.IntervalTree import Node, Interval



class TestIntervalTree(unittest.TestCase):
    def setUp(self):
        self.intervals = [
            Interval(15, 20),
            Interval(10, 30),
            Interval(17, 19),
            Interval(5, 20),
            Interval(12, 15),
            Interval(30, 40)
        ]
        self.idx = BalancedIntervalTree()
        for interval in self.intervals:
            self.idx.insert(interval)


    def test_initial_node(self):
        root = BalancedIntervalTree().insert(Interval(17, 19))
        self.assertEqual(root.max, 19)
        self.assertEqual(root.left, None)
        self.assertEqual(root.right, None)


    def test_inOrder_traversal(self):
        in_order_result = []
        self.idx.inOrderTraversal(self.idx.root, in_order_result)
        result_sorted_intervals = [interval.low for interval in in_order_result]

        self.assertEqual(result_sorted_intervals, sorted([interval.low for interval in self.intervals]))


    def test_build_tree(self):
        in_order_result = []
        self.idx.inOrderTraversal(self.idx.root, in_order_result)

        root = self.idx.buildBalancedTree(in_order_result, 0, len(in_order_result) - 1)

        mid_idx = (0 + len(in_order_result) - 1) // 2
        self.assertEqual(root.interval, in_order_result[mid_idx], "Midpoint node should be correctly calculated.")

        # Test that left and right subtrees are correctly built
        self.assertIsNotNone(root.left, "Left child should not be None.")
        self.assertIsNotNone(root.right, "Right child should not be None.")

        # Test that the right subtree contains the correct node (recursive mid)
        mid_right_idx = (mid_idx + 1 + len(in_order_result) - 1) // 2
        self.assertEqual(root.right.interval, in_order_result[mid_right_idx])

        # Test that the max values are correctly updated
        self.assertEqual(root.max, max([interval.high for interval in in_order_result]))
        # Test if values1 is greater or equal than value2
        self.assertGreaterEqual(root.max, root.interval.high)
        self.assertGreaterEqual(root.max, root.left.max)
        self.assertGreaterEqual(root.max, root.right.max)


    def test_overalp_with_root(self):
        # Test interval overlaps with the root interval (12, 15)
        search_interval = Interval(13, 14)
        # Rebuild tree to balanced one
        self.idx.root = self.idx.rebuildTree(self.idx.root)
        result = self.idx.isOverlapping(self.idx.root, search_interval)
        self.assertEqual(result, Interval(12, 15))


    def test_overlap_with_left_subtree(self):
        search_interval = Interval(18, 25)
        self.idx.root = self.idx.rebuildTree(self.idx.root)
        left_interval = self.idx.root.left.interval
        result = self.idx.isOverlapping(self.idx.root, search_interval)
        self.assertEqual(result, left_interval)



    def test_overlap_with_right_subtree(self):
        search_interval = Interval(36, 40)
        self.idx.root = self.idx.rebuildTree(self.idx.root)
        #print("Tree structure after rebuild:")
        #self.idx.printTree(self.idx.root)

        result = self.idx.isOverlapping(self.idx.root, search_interval)
        self.assertEqual(result, Interval(30, 40))







if __name__ == "__main__":
    unittest.main()


