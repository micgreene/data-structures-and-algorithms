'use strict';

const Edge = require('./edge.js');

//graph tracks a list of edges and their related vertices
class Graph {
  constructor() {
    this.adjacencyList = new Map();//tracks edges as Key(vertex):Value(edge) pairs
  }

  addNode(node) {
    this.adjacencyList.set(node, []); //used to store edges
  }

  addDirectedEdge(startNode, endNode = null, weight = 0) {
    let adjancencies = this.adjacencyList.get(startNode);
    adjancencies.push(new Edge(endNode, weight));
  }

  getNodes() {
    let retObj = [];
    this.adjacencyList.forEach((value, key) => {
      retObj = [...retObj, key];
    });

    if (this.size() === 0) {
      return null;
    }
    return retObj;
  }

  getNeighbors(node) {
    if (this.size() === 0) {
      return null;
    }

    return [...this.adjacencyList.get(node)]; //create a copy of our list and return the copy
  }

  size() {
    let size = 0;
    this.adjacencyList.forEach((value, key) => {
      size++;
    });
    return size;
  }

  breadthFirst() {
    if (this.size() === 0) {
      return null;
    }

    let retList = [];
    let root = this.adjacencyList.keys().next().value;
    let queue = [];
    retList.push(root);

    this.getNeighbors(root).forEach(item => queue.push(item.node));

    while (queue.length > 0) {
      let nextNode = queue.shift();
      retList.push(nextNode);

      this.getNeighbors(nextNode).forEach(item => {
        if (retList.includes(item.node) === false)
          queue.push(item.node);
      });

    }
    return retList;
  }
}

const Node = require('./node');

let graph = new Graph();
let node1 = new Node('a');
let node2 = new Node('b');
let node3 = new Node('c');
let node4 = new Node('d');
let node5 = new Node('e');
let node6 = new Node('f');

graph.addNode(node1);
graph.addNode(node2);
graph.addNode(node3);
graph.addNode(node4);
graph.addNode(node5);
graph.addNode(node6);

graph.addDirectedEdge(node1, node6);
graph.addDirectedEdge(node6, node1);
graph.addDirectedEdge(node6, node3);
graph.addDirectedEdge(node3, node6);
graph.addDirectedEdge(node3, node5);
graph.addDirectedEdge(node5, node3);
graph.addDirectedEdge(node5, node4);
graph.addDirectedEdge(node4, node5);
graph.addDirectedEdge(node4, node2);
graph.addDirectedEdge(node2, node4);

// console.log(graph.getNodes());
console.log(graph.getNeighbors(node4));
// graph.breadthFirst();
console.log(graph.breadthFirst());

module.exports = Graph;
