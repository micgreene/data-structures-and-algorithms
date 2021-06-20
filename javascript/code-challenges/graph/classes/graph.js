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

  getNodes(){
    let retObj = [];
    this.adjacencyList.forEach( (value, key) => {
      retObj = [...retObj, key];
    });

    if(this.size() === 0){
      return null;
    }
    return retObj;
  }

  getNeighbors(node) {
    if(this.size() === 0){
      return null;
    }

    return [...this.adjacencyList.get(node)]; //create a copy of our list and return the copy
  }

  size(){
    let size = 0;
    this.adjacencyList.forEach( (value, key) => {
      size++;
    } );
    return size;
  }
}

module.exports = Graph;
