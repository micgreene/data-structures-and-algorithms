from ..stack import Stack
from ..stack_queue_pseudo import PseudoQueue
import pytest

def test_create_empty_pseudo_queue():
    pq = PseudoQueue()
    with pytest.raises(Exception):
        pq.storage_stack.peek()

def test_enqueue_one():
    pq = PseudoQueue()
    pq.enqueue('A')

    actual = pq.peek()
    expected = 'A'
    assert actual == expected

def test_enqueue_multiple():
    pq = PseudoQueue()
    pq.enqueue('A')
    pq.enqueue('B')
    pq.enqueue('C')
    pq.enqueue('D')
    pq.enqueue('E')

    actual = pq.dequeue()
    expected = 'A'
    assert actual == expected

    actual = pq.peek()
    expected = 'E'
    assert actual == expected

def test_dequeue():
    pq = PseudoQueue()
    pq.enqueue('A')
    pq.enqueue('B')
    pq.enqueue('C')

    actual = pq.dequeue()
    expected = 'A'
    assert actual == expected

def test_peek():
    pq = PseudoQueue()
    pq.enqueue('A')
    pq.enqueue('B')
    pq.enqueue('C')

    actual = pq.peek()
    expected = 'C'
    assert actual == expected

def test_dequeue_until_empty():
    pq = PseudoQueue()
    pq.enqueue('A')
    pq.enqueue('B')
    pq.enqueue('C')

    pq.dequeue()
    pq.dequeue()
    pq.dequeue()

    actual = pq.is_empty()
    expected = True
    assert actual == expected

def test_create_empty_queue():
    pq = PseudoQueue()

    actual = pq.is_empty()
    expected = True
    assert actual == expected

def test_peek_or_dequeue_empty_queue():
    pq = PseudoQueue()

    with pytest.raises(Exception):
        pq.peek()

    with pytest.raises(Exception):
        pq.dequeue()
