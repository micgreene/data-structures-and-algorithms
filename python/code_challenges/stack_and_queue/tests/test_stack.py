from ..stack import Stack
import pytest

def test_push_one():
    stack = Stack()
    stack.push('A')

    actual = stack.peek()
    expected = 'A'
    assert actual == expected

def test_push_multiple():
    stack = Stack()
    stack.push('A')
    stack.push('B')
    stack.push('C')
    stack.push('D')
    stack.push('E')

    actual = stack.peek()
    expected = 'E'
    assert actual == expected

def test_pop_stack():
    stack = Stack()
    stack.push('A')
    stack.push('B')
    stack.push('C')

    actual = stack.pop()
    expected = 'C'
    assert actual == expected

def test_pop_stack_until_empty():
    stack = Stack()
    stack.push('A')
    stack.push('B')
    stack.push('C')

    stack.pop()
    stack.pop()
    stack.pop()
    actual = stack.is_empty()
    expected = True
    assert actual == expected

def test_peek():
    stack = Stack()
    stack.push('A')
    stack.push('B')
    stack.push('C')

    actual = stack.peek()
    expected = 'C'
    assert actual == expected

def test_create_empty_stack():
    stack = Stack()
    actual = stack.is_empty()
    expected = True
    assert actual == expected

def test_peek_pop_empty_stack():
    stack = Stack()

    with pytest.raises(Exception):
        stack.peek()

    with pytest.raises(Exception):
        stack.pop()
