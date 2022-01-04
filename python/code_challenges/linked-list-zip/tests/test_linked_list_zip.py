import sys

sys.path.append('/home/micgreene/codefellows/301/data-structures-and-algorithms/python/code_challenges/linked-list/linked_list')

from linked_list import Node, Linked_List
from linked_list_zip import __version__
from linked_list_zip.linked_list_zip import zip_lists

def test_version():
    assert __version__ == '0.1.0'

def test_lists_zip():
    test_list1 = Linked_List()
    test_list1.insert(1)
    test_list1.append(3)
    test_list1.append(5)
    test_list2 = Linked_List()
    test_list2.insert(2)
    test_list2.append(4)
    test_list2.append(6)

    actual = zip_lists(test_list1, test_list2).to_string()
    expected = '{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> { 6 } -> NONE'
    assert actual == expected

def test_both_lists_empty():
    test_list1 = Linked_List()
    test_list2 = Linked_List()

    actual = zip_lists(test_list1, test_list2)
    expected = None
    assert actual == expected

def test_one_list_empty():
    test_list1 = Linked_List()
    test_list2 = Linked_List()
    test_list2.insert(2)
    test_list2.append(4)
    test_list2.append(6)

    actual = zip_lists(test_list1, test_list2).to_string()
    expected = '{ 2 } -> { 4 } -> { 6 } -> NONE'
    assert actual == expected

def test_one_list_short():
    test_list1 = Linked_List()
    test_list1.insert(1)
    test_list1.append(3)
    test_list1.append(5)
    test_list1.append(6)
    test_list2 = Linked_List()
    test_list2.insert(2)
    test_list2.append(4)

    actual = zip_lists(test_list1, test_list2).to_string()
    expected = '{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> { 6 } -> NONE'
    assert actual == expected
