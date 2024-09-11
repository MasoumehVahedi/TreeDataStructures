from TreeDataStructure.src.BTree_BalancedTree import BTree


def main():
    btree = BTree(min_degree=3)

    # Insert key-value pairs into the B-tree
    for i in range(20):
        btree.insert((i, 2 * i))

    btree.printBTree(btree.root)

    # Search for a key in the B-tree
    search_result = btree.search(8)
    if search_result is not None:
        node, index = search_result
        print(f"\nKey 8 found in the B-tree at node: {node}, index: {index}.")
    else:
        print("\nKey 8 not found in the B-tree.")


if __name__ == "__main__":
    main()