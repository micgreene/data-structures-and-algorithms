from code_challenges.graph_business_trip.graph_business_trip import business_trip
from code_challenges.graph_business_trip.graph import Graph
import pytest

def test_business_trip():
    graph_map = Graph()
    ny = test_graph.add_node('New York')
    nash = test_graph.add_node('Nashville')
    cin = test_graph.add_node('Cicinnati')
    dal = test_graph.add_node('Dallas')
    la = test_graph.add_node('Los Angeles')

    test_graph.add_edge(ny, nash, 400)
    test_graph.add_edge(nash, ny, 400)
    test_graph.add_edge(nash, cin, 375)
    test_graph.add_edge(cin, nash, 375)
    test_graph.add_edge(cin, dal, 450)
    test_graph.add_edge(dal, cin, 450)
    test_graph.add_edge(dal, la, 575)
    test_graph.add_edge(la, dal, 575)

    itinerary = ['New York', 'Nashville','Cicinnati', 'Dallas']
    actual = business_trip(graph_map, itinerary)
    expected = f'[True, $1225]'
    assert actual == expected
