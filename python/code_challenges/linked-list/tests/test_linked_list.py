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
