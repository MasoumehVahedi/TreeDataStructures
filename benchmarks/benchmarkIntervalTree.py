from TreeDataStructure.src.IntervalTree import Interval, UnbalancedIntervalTree
from TreeDataStructure.src.IntervalTree_balanced import BalancedIntervalTree



def main():
    intervals = [
        Interval(15, 20),
        Interval(10, 30),
        Interval(17, 19),
        Interval(5, 20),
        Interval(12, 15),
        Interval(30, 40)
    ]

    # ----------------------------------------------------------------------- #
    #                   Unbalanced Interval Tree
    # ----------------------------------------------------------------------- #
    unbalanced_tree = UnbalancedIntervalTree()
    for interval in intervals:
        unbalanced_tree.insert(interval)

    print("InOrder traversal of unbalanced Interval Tree:")
    unbalanced_tree.inOrder(unbalanced_tree.root)

    unbalanced_tree.printTree(unbalanced_tree.root)

    # Search for overlapping interval
    query = Interval(6, 7)
    print(f"\nSearching for overlapping interval with {query}")
    result = unbalanced_tree.isOverlapping(unbalanced_tree.root, query)
    if result:
        print(f"Overlaps with {result}")
    else:
        print("No overlap found")

    # ----------------------------------------------------------------------- #
    #                   Balanced Interval Tree
    # ----------------------------------------------------------------------- #
    balanced_tree = BalancedIntervalTree()
    for interval in intervals:
        balanced_tree.insert(interval)

    # Print the unbalanced tree
    print("Unbalanced Interval Tree:")
    balanced_tree.printTree()

    # Rebuild the tree to balance it
    balanced_tree.root = balanced_tree.rebuildTree(balanced_tree.root)

    # Print the balanced tree
    print("\nBalanced Interval Tree:")
    balanced_tree.printTree()

    # Search for an overlapping interval
    query = Interval(6, 7)
    result = balanced_tree.isOverlapping(balanced_tree.root, query)
    if result:
        print(f"\nFound overlapping interval: {result}")
    else:
        print(f"\nNo overlapping interval found for {query}")


if __name__ == "__main__":
    main()
