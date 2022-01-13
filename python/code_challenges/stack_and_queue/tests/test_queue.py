from ..queue import Queue
import pytest

def test_enqueue_one():
    queue = Queue()
    queue.enqueue('A')

    actual = queue.peek()
    expected = 'A'
    assert actual == expected

def test_enqueue_multiple():
    queue = Queue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    queue.enqueue('D')
    queue.enqueue('E')

    actual = queue.front.value
    expected = 'A'
    assert actual == expected

    actual = queue.back.value
    expected = 'E'
    assert actual == expected

def test_dequeue():
    queue = Queue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')

    actual = queue.dequeue()
    expected = 'A'
    assert actual == expected

def test_peek():
    queue = Queue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')

    actual = queue.peek()
    expected = 'A'
    assert actual == expected

def test_dequeue_until_empty():
    queue = Queue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')

    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    actual = queue.is_empty()
    expected = True
    assert actual == expected

def test_create_empty_queue():
    queue = Queue()

    actual = queue.is_empty()
    expected = True
    assert actual == expected

def test_peek_or_dequeue_empty_queue():
    queue = Queue()

    with pytest.raises(Exception):
        queue.peek()

    with pytest.raises(Exception):
        queue.dequeue()
