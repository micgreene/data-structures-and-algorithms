from ..node import Node

import pytest

def test_node_created():
    node = Node('A')

    actual = node.value
    expected = 'A'

    assert actual == expected


def test_empty_node_created():
    node = Node()

    actual = node.value
    expected = None

    assert actual == expected
