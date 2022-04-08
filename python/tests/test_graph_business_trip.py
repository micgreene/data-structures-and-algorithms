from code_challenges.graph_business_trip.graph_business_trip import business_trip
from code_challenges.graph_business_trip.graph import Graph
import pytest

def test_business_trip():
    graph_map = Graph()
    ny = graph_map.add_node('New York')
    nash = graph_map.add_node('Nashville')
    cin = graph_map.add_node('Cicinnati')
    dal = graph_map.add_node('Dallas')
    la = graph_map.add_node('Los Angeles')

    graph_map.add_edge(ny, nash, 400)
    graph_map.add_edge(nash, ny, 400)
    graph_map.add_edge(nash, cin, 375)
    graph_map.add_edge(cin, nash, 375)
    graph_map.add_edge(cin, dal, 450)
    graph_map.add_edge(dal, cin, 450)
    graph_map.add_edge(dal, la, 575)
    graph_map.add_edge(la, dal, 575)

    itinerary = ['New York', 'Nashville','Cicinnati', 'Dallas']
    actual = business_trip(graph_map, itinerary)
    expected = [True, '$1225']
    assert actual == expected

def test_business_trip_fail():
    graph_map = Graph()
    ny = graph_map.add_node('New York')
    nash = graph_map.add_node('Nashville')
    cin = graph_map.add_node('Cicinnati')
    dal = graph_map.add_node('Dallas')
    la = graph_map.add_node('Los Angeles')

    graph_map.add_edge(ny, nash, 400)
    graph_map.add_edge(nash, ny, 400)
    graph_map.add_edge(nash, cin, 375)
    graph_map.add_edge(cin, nash, 375)
    graph_map.add_edge(cin, dal, 450)
    graph_map.add_edge(dal, cin, 450)
    graph_map.add_edge(dal, la, 575)
    graph_map.add_edge(la, dal, 575)

    itinerary = ['New York', 'Nashville','Cicinnati', 'Los Angeles']
    actual = business_trip(graph_map, itinerary)
    expected = [False, '$0']
    assert actual == expected

def test_empty_itinerary():
    graph_map = Graph()
    ny = graph_map.add_node('New York')
    nash = graph_map.add_node('Nashville')
    cin = graph_map.add_node('Cicinnati')
    dal = graph_map.add_node('Dallas')
    la = graph_map.add_node('Los Angeles')

    graph_map.add_edge(ny, nash, 400)
    graph_map.add_edge(nash, ny, 400)
    graph_map.add_edge(nash, cin, 375)
    graph_map.add_edge(cin, nash, 375)
    graph_map.add_edge(cin, dal, 450)
    graph_map.add_edge(dal, cin, 450)
    graph_map.add_edge(dal, la, 575)
    graph_map.add_edge(la, dal, 575)

    itinerary = []
    actual = business_trip(graph_map, itinerary)
    expected = [False, '$0']
    assert actual == expected

def test_empty_map():
    graph_map = Graph()
    ny = graph_map.add_node('New York')

    itinerary = ['New York', 'Nashville','Cicinnati', 'Los Angeles']
    actual = business_trip(graph_map, itinerary)
    expected = [False, '$0']
    assert actual == expected

def test_business_round_trip():
    graph_map = Graph()
    ny = graph_map.add_node('New York')
    nash = graph_map.add_node('Nashville')
    cin = graph_map.add_node('Cicinnati')
    dal = graph_map.add_node('Dallas')
    la = graph_map.add_node('Los Angeles')

    graph_map.add_edge(ny, nash, 400)
    graph_map.add_edge(nash, ny, 400)
    graph_map.add_edge(nash, cin, 375)
    graph_map.add_edge(cin, nash, 375)
    graph_map.add_edge(cin, dal, 450)
    graph_map.add_edge(dal, cin, 450)
    graph_map.add_edge(dal, la, 575)
    graph_map.add_edge(la, dal, 575)

    itinerary = ['New York', 'Nashville','Cicinnati', 'Dallas', 'Los Angeles', 'Dallas', 'Cicinnati', 'Nashville', 'New York']
    actual = business_trip(graph_map, itinerary)
    expected = [True, '$3600']
    assert actual == expected
