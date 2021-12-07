# Graphs
<!-- Short summary or background information -->

+ A Graph is a collection of vertices, called 'Nodes', contained in an ES6 Map object as a Key:Value pair list.

+ The Key of each object in the map is the node and the Value is an array which contains any other nodes it shares adjacency with and if there is a 'Weight' assigned to that edge.

## Challenge
<!-- Description of the challenge -->

+ 35: Implement your own Graph. The graph should be represented as an adjacency list.

+ 36: Write the following method for the Graph class:

  + breadthFirst
    + Arguments: Node
    + Return: A collection of nodes in the order they were visited.
  + Display the collection

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

+ For this assignment I used TDD to move through the assigned methods.
  + First I listed out the test cases and what each required.
  + Then I implmented the requirements for each in the methods as I went until everything was passing.

## API
<!-- Description of each method publicly available in your Graph -->

+ AddNode()
  + Adds a new node to the graph
  + Takes in the value of that node
  + Returns the added node

+ AddEdge()
  + Adds a new edge between two nodes in the graph
  + Include the ability to have a “weight”
  + Takes in the two nodes to be connected by the edge
  + Both nodes should already be in the Graph

+ GetNodes()
  + Returns all of the nodes in the graph as a collection (set, list, or similar)

+ GetNeighbors()
  + Returns a collection of edges connected to the given node
  + Takes in a given node
  + Include the weight of the connection in the returned collection

+ Size()
  + Returns the total number of nodes in the graph