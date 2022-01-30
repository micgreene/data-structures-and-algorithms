from code_challenges.trees.binary_search_tree import BinarySearch
import pytest

def test_create_empty_tree():
    actual = BinarySearch()

    assert actual

def test_create_tree_only_root():
    bst = BinarySearch(7)

    actual = bst.root.value
    print(actual)
    expected = 7

    assert actual == expected

def test_add_to_tree():
    bst = BinarySearch(5)
    bst.add(3)
    bst.add(7)

    actual = bst.root.left.value
    expected = 3
    assert actual == expected

    actual = bst.root.right.value
    expected = 7
    assert actual == expected

def test_create_tree_only_root():
    bst = BinarySearch(7)

    actual = bst.root.value
    expected = 7

    assert actual == expected

def test_pre_order():
    bst = BinarySearch(7)
    bst.add(5)
    bst.add(9)
    bst.add(4)
    bst.add(6)
    bst.add(8)
    bst.add(10)

    actual = bst.pre_order()
    expected = [7,5,4,6,9,8,10]

    assert actual == expected

def test_in_order():
    bst = BinarySearch(7)
    bst.add(5)
    bst.add(9)
    bst.add(4)
    bst.add(6)
    bst.add(8)
    bst.add(10)

    actual = bst.in_order()
    expected = [4,5,6,7,8,9,10]

    assert actual == expected

def test_post_order():
    bst = BinarySearch(7)
    bst.add(5)
    bst.add(9)
    bst.add(4)
    bst.add(6)
    bst.add(8)
    bst.add(10)

    actual = bst.post_order()
    expected = [4,6,5,8,10,9,7]

    assert actual == expected

def test_contains():
    bst = BinarySearch(7)
    bst.add(5)
    bst.add(9)
    bst.add(4)
    bst.add(6)
    bst.add(8)
    bst.add(10)

    actual = bst.contains(10)
    expected = True
    assert actual == expected

    actual = bst.contains(11)
    expected = False
    assert actual == expected
