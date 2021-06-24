'use strict';

const Graph = require('../classes/graph.js');
const Node = require('../classes/node.js');

describe('GRAPH CLASS TESTS', () => {
  //create an instance of the graph class to test
  let graph = new Graph();

  //make a bunch of nodes
  const a = new Node('a');
  const b = new Node('b');
  const c = new Node('c');
  const d = new Node('d');
  const e = new Node('e');
  const f = new Node('f');

  //resets the graph for each test
  beforeEach(() => {
    //reset the graph
    graph = new Graph();

    //re-add all the Nodes
    graph.addNode(a);
    graph.addNode(b);
    graph.addNode(c);
    graph.addNode(d);
    graph.addNode(e);
    graph.addNode(f);

    //create Edge relationships between them
    graph.addDirectedEdge(a, b);
    graph.addDirectedEdge(b, a);
    graph.addDirectedEdge(b, c);
    graph.addDirectedEdge(c, b);
    graph.addDirectedEdge(c, d);
    graph.addDirectedEdge(d, c);
    graph.addDirectedEdge(d, e);
    graph.addDirectedEdge(e, f);
  });

  //test case #1
  it('Node can be successfully added to the graph', () => {
    //add Node to graph
    const g = new Node('g');
    graph.addNode(g);

    expect(graph.getNodes()).toContain(g);
  });

  //test case #2
  it('An edge can be successfully added to the graph', () => {
    //add Node to graph
    const g = new Node('g');
    graph.addNode(g);
    graph.addDirectedEdge(f, g);
    graph.addDirectedEdge(g, f);

    expect(graph.getNeighbors(g)[0].node).toEqual(f);
  });

  //test case #3
  it('A collection of all nodes can be properly retrieved from the graph', () => {
    expect(graph.getNodes()).toEqual(
      [
        { 'value': 'a' },
        { 'value': 'b' },
        { 'value': 'c' },
        { 'value': 'd' },
        { 'value': 'e' },
        { 'value': 'f' }
      ]);
  });

  //test case #4
  it('All appropriate neighbors can be retrieved from the graph', () => {
    expect(graph.getNeighbors(d)[0].node).toEqual(c);
    expect(graph.getNeighbors(d)[1].node).toEqual(e);
  });

  //test case #5
  it('Neighbors are returned with the weight between nodes included', () => {
    const g = new Node('g');
    graph.addNode(g);
    graph.addDirectedEdge(f, g, 5);
    graph.addDirectedEdge(g, f, 10);

    expect(graph.getNeighbors(g)[0].weight).toEqual(10);
  });

  //test case #6
  it('The proper size is returned, representing the number of nodes in the graph', () => {
    expect(graph.size()).toEqual(6);
  });

  //test case #7
  it('A graph with only one node and edge can be properly returned', () => {
    //reset graph
    graph = new Graph();

    //add a single node and edge to the graph
    graph.addNode(a);
    graph.addDirectedEdge(a);

    expect(graph.getNodes()).toEqual([{'value': 'a'}]);
    expect(graph.getNeighbors(a)).toEqual([{'node': null, 'weight': 0}]);
  });

  //test case #8
  it('An empty graph properly returns null', () => {
    //reset graph
    graph = new Graph();

    expect(graph.getNodes()).toEqual(null);
  });

  //test case #9
  it('Can be traversed breadth-first, returning an array of nodes encountered in order', () => {
    //reset graph
    graph = new Graph();

    graph.addNode(a);
    graph.addNode(b);
    graph.addNode(c);
    graph.addNode(d);
    graph.addNode(e);
    graph.addNode(f);

    graph.addDirectedEdge(a, f);
    graph.addDirectedEdge(f, a);
    graph.addDirectedEdge(f, c);
    graph.addDirectedEdge(c, f);
    graph.addDirectedEdge(c, e);
    graph.addDirectedEdge(e, c);
    graph.addDirectedEdge(e, d);
    graph.addDirectedEdge(d, e);
    graph.addDirectedEdge(d, b);
    graph.addDirectedEdge(b, d);

    expect(graph.breadthFirst()).toEqual( [
      {'value': 'a'},
      {'value': 'f'},
      {'value': 'c'},
      {'value': 'e'},
      {'value': 'd'},
      {'value': 'b'}
    ]);
  });

  //test case #10
  it('Trying to traverse breadth-first through an empty graph properly returns null', () => {
    //reset graph
    graph = new Graph();

    expect(graph.breadthFirst()).toEqual(null);
  });

  //test case #11
  it('Trying to traverse breadth-first through a graph with a single item returns a single node', () => {
    //reset graph
    graph = new Graph();

    graph.addNode(a);

    expect(graph.breadthFirst()).toEqual([{'value': 'a'}]);
  });

  //test case #12
  it('Trying to traverse breadth-first through a graph with no edges returns a single node', () => {
    //reset graph
    graph = new Graph();

    graph.addNode(a);
    graph.addNode(b);

    expect(graph.breadthFirst()).toEqual([{'value': 'a'}]);
  });
});
