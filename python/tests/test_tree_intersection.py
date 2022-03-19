from code_challenges.tree_intersection.tree_int import tree_intersection
from code_challenges.tree_intersection.binary_search_tree import BinarySearch
import pytest

def test_tree_intersection():
    tree1 = BinarySearch()
    tree2 = BinarySearch()

    tree1.add(2)
    tree1.add(4)
    tree1.add(6)
    tree1.add(8)
    tree1.add(10)
    tree1.add(11)

    tree2.add(1)
    tree2.add(3)
    tree2.add(5)
    tree2.add(7)
    tree2.add(9)
    tree2.add(11)

    actual = tree_intersection(tree1, tree2)
    expected = [11]

    assert actual == expected

def test_no_tree_intersection():
    tree1 = BinarySearch()
    tree2 = BinarySearch()

    tree1.add(2)
    tree1.add(4)
    tree1.add(6)
    tree1.add(8)
    tree1.add(10)

    tree2.add(1)
    tree2.add(3)
    tree2.add(5)
    tree2.add(7)
    tree2.add(9)

    actual = tree_intersection(tree1, tree2)
    expected = []

    assert actual == expected

def test_string_tree_intersection():
    with pytest.raises(Exception):
        tree1 = BinarySearch()
        tree2 = BinarySearch()

        tree1.add(2)
        tree1.add(4)
        tree1.add(6)
        tree1.add(8)
        tree1.add(10)

        tree2.add(1)
        tree2.add(3)
        tree2.add(5)
        tree2.add('B')
        tree2.add(9)

        tree_intersection(tree1, tree2)
