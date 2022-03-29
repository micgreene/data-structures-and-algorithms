from code_challenges.graph.graph import Graph

import pytest

'''
Node can be successfully added to the graph
An edge can be successfully added to the graph
A collection of all nodes can be properly retrieved from the graph
All appropriate neighbors can be retrieved from the graph
Neighbors are returned with the weight between nodes included
The proper size is returned, representing the number of nodes in the graph
A graph with only one node and edge can be properly returned
An empty graph properly returns null
'''
def test_add_node():
    test_graph = Graph()
    node1 = test_graph.add_node(1)

    actual = test_graph
    expected = 'a graph defined as:\n{Vertex(1): []}'



# test_graph = Graph()

# node1 = test_graph.add_node(1)
# node2 = test_graph.add_node(2)
# node3 = test_graph.add_node(3)
# node4 = test_graph.add_node(4)
# node5 = test_graph.add_node(5)

# test_graph.add_edge(node1, node2,1)
# test_graph.add_edge(node2, node3,2)
# test_graph.add_edge(node2, node5,6)
# test_graph.add_edge(node3, node4,3)
# test_graph.add_edge(node4, node5,4)
# test_graph.add_edge(node5, node1,5)

# print(f'My graph:\n{test_graph}\n')

# print(f'get_nodes(): {test_graph.get_nodes()}\n')

# print(f'get_neighbors(): {test_graph.get_neighbors(node2)}\n')

# print(f'size(): {test_graph.size()}')
