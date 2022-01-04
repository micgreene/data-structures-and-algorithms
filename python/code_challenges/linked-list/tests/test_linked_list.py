from linked_list import __version__
from linked_list.linked_list import Linked_List, Node
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_empty_list():
    actual = Linked_List()
    expected = None
    assert actual.head == expected

def test_insert_list():
    test_list = Linked_List()
    test_list.insert(5)
    actual = test_list.head.value
    expected = 5
    assert actual == expected

def test_head_value():
    test_list = Linked_List()
    test_list.insert(4)
    actual = str(test_list.head)
    expected = 'The Node with a value of 4'
    assert actual == expected

def test_insert_multiple():
    test_list = Linked_List()
    test_list.insert(5)
    test_list.insert(4)
    test_list.insert(7)
    actual = test_list.head.value
    expected = 7
    assert actual == expected
    actual = test_list.to_string()
    expected = '{ 7 } -> { 4 } -> { 5 } -> NONE'
    assert actual == expected

def test_includes_true():
    test_list = Linked_List()
    test_list.insert(5)
    test_list.insert(4)
    test_list.insert(7)
    actual = test_list.includes(4)
    expected = True
    assert actual == expected

def test_includes_false():
    test_list = Linked_List()
    test_list.insert(5)
    test_list.insert(4)
    test_list.insert(7)
    actual = test_list.includes(47)
    expected = False
    assert actual == expected

def test_to_string():
    test_list = Linked_List()
    test_list.insert(5)
    test_list.insert(4)
    test_list.insert(7)
    actual = test_list.to_string()
    expected = '{ 7 } -> { 4 } -> { 5 } -> NONE'
    assert actual == expected

<<<<<<< HEAD
def test_k_greater_than_list_len():
    with pytest.raises(ValueError):
        test_list = Linked_List()
        test_list.insert(5)
        test_list.insert(4)
        test_list.insert(7)
        actual = test_list.kthfromend(4)


def test_k_equal_to_list_len():
    with pytest.raises(ValueError):
        test_list = Linked_List()
        test_list.insert(5)
        test_list.insert(4)
        test_list.insert(7)
        actual = test_list.kthfromend(3)

# “Happy Path” where k is not at the end, but somewhere in the middle of the linked list

def test_k_not_positive():
    test_list = Linked_List()
    test_list.insert(5)
    test_list.insert(4)
    test_list.insert(7)
    test_list.insert(11)
    test_list.insert(15)
    actual = test_list.kthfromend(3)
    expected = 11
    assert actual == expected

def test_list_is_len_of_one():
    test_list = Linked_List()
    test_list.insert(5)
    actual = test_list.kthfromend(0)
    expected = 5
    assert actual == expected

def test_k_happy_path():
    test_list = Linked_List()
    test_list.insert(5)
    test_list.insert(4)
    test_list.insert(7)
    test_list.insert(11)
    test_list.insert(15)
    test_list.insert(18)
    test_list.insert(21)
    test_list.insert(25)
    test_list.insert(28)
    test_list.insert(32)
    test_list.insert(39)
    actual = test_list.kthfromend(5)
    expected = 18
    assert actual == expected
=======
'''
Can successfully insert a node after the last node of the linked list
'''

def test_append():
    test_list = Linked_List()
    test_list.append(5)
    actual = test_list.head.value
    expected = 5
    assert actual == expected

def test_multiple_append():
    test_list = Linked_List()
    test_list.append(5)
    test_list.append(4)
    test_list.append(7)
    actual = test_list.to_string()
    expected = '{ 5 } -> { 4 } -> { 7 } -> NONE'
    assert actual == expected

def test_insert_before():
    test_list = Linked_List()
    test_list.append(5)
    test_list.append(4)
    test_list.append(7)
    test_list.insert_before(9, 4)
    actual = test_list.to_string()
    expected = '{ 5 } -> { 9 } -> { 4 } -> { 7 } -> NONE'
    assert actual == expected

def test_insert_before_head():
    test_list = Linked_List()
    test_list.append(5)
    test_list.append(4)
    test_list.append(7)
    test_list.insert_before(9, 5)
    actual = test_list.to_string()
    expected = '{ 9 } -> { 5 } -> { 4 } -> { 7 } -> NONE'
    assert actual == expected

def test_insert_after():
    test_list = Linked_List()
    test_list.append(5)
    test_list.append(4)
    test_list.append(7)
    test_list.insert_after(9, 4)
    actual = test_list.to_string()
    expected = '{ 5 } -> { 4 } -> { 9 } -> { 7 } -> NONE'
    assert actual == expected

def test_insert_after_tail():
    test_list = Linked_List()
    test_list.append(5)
    test_list.append(4)
    test_list.append(7)
    test_list.insert_after(9, 7)
    actual = test_list.to_string()
    expected = '{ 5 } -> { 4 } -> { 7 } -> { 9 } -> NONE'
    assert actual == expected

def test_insert_out_of_range():
    test_list = Linked_List()
    test_list.append(5)
    test_list.append(4)
    test_list.append(7)

    with pytest.raises(ValueError):
        test_list.insert_after(9, 9)


>>>>>>> 0ebef2e243ba349140ac968fbd4ceec5089ecdb6
