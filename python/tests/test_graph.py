from code_challenges.graph.graph import Graph

import pytest

def test_add_node():
    test_graph = Graph()
    node1 = test_graph.add_node(1)

    actual = str(test_graph)
    expected = 'a graph defined as:\n{Vertex(1): []}'
    assert actual == expected

def test_add_edge():
    test_graph = Graph()
    node1 = test_graph.add_node(1)
    node2 = test_graph.add_node(2)
    test_graph.add_edge(node1, node2, 5)

    actual = str(test_graph.adj_list[node1][0])
    expected = f'an edge between a node vertex with a value of {1} and a node vertex with a value of {2}, with a weight of {5}'
    assert actual == expected

def test_get_nodes():
    test_graph = Graph()
    node1 = test_graph.add_node(1)
    node2 = test_graph.add_node(2)

    actual = str(test_graph.get_nodes())
    expected = f'[Vertex(1), Vertex(2)]'
    assert actual == expected

def test_get_neighbors():
    test_graph = Graph()
    node1 = test_graph.add_node(1)
    node2 = test_graph.add_node(2)
    node3 = test_graph.add_node(3)

    test_graph.add_edge(node1, node2, 1)
    test_graph.add_edge(node2, node3, 2)
    test_graph.add_edge(node3, node1, 3)

    actual = str(test_graph.get_neighbors(node1))
    expected = f'[Edge((Vertex(1), Vertex(2), 1))]'
    assert actual == expected

    actual = str(test_graph.get_neighbors(node2))
    expected = f'[Edge((Vertex(2), Vertex(3), 2))]'
    assert actual == expected

    actual = str(test_graph.get_neighbors(node3))
    expected = f'[Edge((Vertex(3), Vertex(1), 3))]'
    assert actual == expected

def test_size():
    test_graph = Graph()
    node1 = test_graph.add_node(1)
    node2 = test_graph.add_node(2)
    node3 = test_graph.add_node(3)

    actual = test_graph.size()
    expected = 3
    assert actual == expected

def test_one_node_one_edge():
    test_graph = Graph()
    node1 = test_graph.add_node(1)
    test_graph.add_edge(node1, None, 5)

    actual = str(test_graph.adj_list[node1][0])
    expected = f'an edge between a node vertex with a value of {1} and {None}, with a weight of {5}'
    assert actual == expected

    actual = str(test_graph)
    expected = f'a graph defined as:\n{{Vertex(1): [Edge((Vertex(1), None, 5))]}}'
    assert actual == expected

def test_one_node_one_edge():
    test_graph = Graph()

    actual = str(test_graph)
    expected = f'a graph defined as:\n{{}}'
    assert actual == expected

def test_breadth_first():
    test_graph = Graph()
    node1 = test_graph.add_node(1)
    node2 = test_graph.add_node(2)
    node3 = test_graph.add_node(3)

    test_graph.add_edge(node1, node2, 1)
    test_graph.add_edge(node2, node3, 2)
    test_graph.add_edge(node3, node1, 3)

    actual = str(test_graph.breadth_first(node1))
    expected = f'[Vertex(1), Vertex(2), Vertex(3)]'
    assert actual == expected

def test_breadth_first_multiple_edges():
    test_graph = Graph()
    node1 = test_graph.add_node(1)
    node2 = test_graph.add_node(2)
    node3 = test_graph.add_node(3)

    test_graph.add_edge(node1, node2, 1)
    test_graph.add_edge(node1, node3, 4)
    test_graph.add_edge(node2, node3, 2)
    test_graph.add_edge(node2, node1, 5)
    test_graph.add_edge(node3, node1, 3)
    test_graph.add_edge(node3, node2, 6)

    actual = str(test_graph.breadth_first(node1))
    expected = f'[Vertex(1), Vertex(2), Vertex(3)]'
    assert actual == expected

def test_breadth_first_disconnected():
    test_graph = Graph()
    node1 = test_graph.add_node(1)
    node2 = test_graph.add_node(2)
    node3 = test_graph.add_node(3)

    actual = str(test_graph.breadth_first(node1))
    expected = f'[Vertex(1)]'
    assert actual == expected

def test_breadth_first_empty():
    test_graph = Graph()

    actual = str(test_graph.breadth_first(None))
    expected = f'[None]'
    assert actual == expected

def test_depth_first():
    test_graph = Graph()
    node1 = test_graph.add_node(1)
    node2 = test_graph.add_node(2)
    node3 = test_graph.add_node(3)

    test_graph.add_edge(node1, node2, 1)
    test_graph.add_edge(node2, node3, 2)
    test_graph.add_edge(node3, node1, 3)

    actual = str(test_graph.depth_first(node1))
    expected = f'[Vertex(1), Vertex(2), Vertex(3)]'
    assert actual == expected

def test_depth_first_multiple_edges():
    test_graph = Graph()

    nodeA = test_graph.add_node('A')
    nodeB = test_graph.add_node('B')
    nodeC = test_graph.add_node('C')
    nodeD = test_graph.add_node('D')
    nodeE = test_graph.add_node('E')
    nodeF = test_graph.add_node('F')
    nodeG = test_graph.add_node('G')
    nodeH = test_graph.add_node('H')

    test_graph.add_edge(nodeA, nodeD, 1)
    test_graph.add_edge(nodeA, nodeB, 2)
    test_graph.add_edge(nodeB, nodeD, 3)
    test_graph.add_edge(nodeB, nodeC, 4)
    test_graph.add_edge(nodeC, nodeG, 5)
    test_graph.add_edge(nodeD, nodeF, 6)
    test_graph.add_edge(nodeD, nodeH, 7)
    test_graph.add_edge(nodeD, nodeE, 8)
    test_graph.add_edge(nodeF, nodeH, 9)

    actual = str(test_graph.depth_first(nodeA))
    expected = f'[Vertex(A), Vertex(B), Vertex(C), Vertex(G), Vertex(D), Vertex(E), Vertex(H), Vertex(F)]'
    assert actual == expected

def test_depth_first_disconnected():
    test_graph = Graph()
    node1 = test_graph.add_node(1)
    node2 = test_graph.add_node(2)
    node3 = test_graph.add_node(3)

    actual = str(test_graph.depth_first(node1))
    expected = f'[Vertex(1)]'
    assert actual == expected

def test_depth_first_empty():
    test_graph = Graph()

    actual = str(test_graph.depth_first(None))
    expected = f'[None]'
    assert actual == expected
