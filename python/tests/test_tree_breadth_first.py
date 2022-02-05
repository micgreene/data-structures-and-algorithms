from code_challenges.tree_breadth_first.tree_breadth_first import BinarySearch
from code_challenges.tree_breadth_first.tree_breadth_first import breadth_first
import pytest


def test_breadth_first_empty_tree():
    test_tree = BinarySearch()
    with pytest.raises(Exception):
        breadth_first(test_tree)

def test_breadth_first():
        test_tree = BinarySearch()
        test_tree.add(5)
        test_tree.add(3)
        test_tree.add(2)
        test_tree.add(4)
        test_tree.add(7)
        test_tree.add(6)
        test_tree.add(8)

        actual = breadth_first(test_tree)
        expected = [5,3,7,2,4,6,8]
        assert actual == expected

def test_breadth_first_negatives():
        test_tree = BinarySearch()
        test_tree.add(-5)
        test_tree.add(-3)
        test_tree.add(-2)
        test_tree.add(-4)
        test_tree.add(-7)
        test_tree.add(-6)
        test_tree.add(-8)

        actual = breadth_first(test_tree)
        expected = [-5,-7,-3,-8,-6,-4,-2]
        assert actual == expected

def test_breadth_first_only_root():
        test_tree = BinarySearch()
        test_tree.add(5)

        actual = breadth_first(test_tree)
        expected = [5]
        assert actual == expected


