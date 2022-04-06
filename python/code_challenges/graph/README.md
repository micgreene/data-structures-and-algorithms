# Graph Class

## Implement Breadth-First Traversal

### Challenge 2

+ Write the following method for the Graph class:
  + **breadth_first**
    + Arguments: Node
    + Return: A collection of nodes in the order they were visited.
    + Display the collection

### Approach & Efficiency

+ I started by creating an image on a whiteboard of a graph.
+ I used a queue data structure as it was helpful for breadth-first traversal in trees.
+ I reasoned in the same way as in a tree, we would enqueue the nodes as we discover them, thus ensuring we add the node as we discover them in order.
+ The challenge for working with graphs was the fact that, unlike in a tree, we may encounter the same node multiple times.
+ This meant we needed to check that we weren't trying to add the same nodes over and over again as we traverse.
+ After I figured out the necessary logic, the rest was simple.

## Implement a Graph

### Challenge 1

+ The graph should be represented as an adjacency list, and should include the following methods:
  + **add node**
    + Arguments: value
    + Returns: The added node
    + Add a node to the graph
  + **add edge**
    + Arguments: 2 nodes to be connected by the edge, weight (optional)
    + Returns: nothing
    + Adds a new edge between two nodes in the graph
    + If specified, assign a weight to the edge
    + Used nodes should already be in the Graph
  + **get nodes**
    + Arguments: none
    + Returns all of the nodes in the graph as a collection (set, list, or similar)
  + **get neighbors**
    + Arguments: node
    + Returns a collection of edges connected to the given node
    + Include the weight of the connection in the returned collection
  + **size**
    + Arguments: none
    + Returns the total number of nodes in the graph

### Approach & Efficiency

+ I started by creating the `add_node()` function and ensuring it could create the expected data structure and store data properly.
+ I did some initial testing with hard coded values to first make sure that `add_edge()` was working correctly, then I did some more as I added `get_nodes()`. Once all tests were passing I continued.
+ I then created `get_neighbors()` last since that was the hardest part, but with the adjacency list completed it was a lot easier to iterate through the nodes.
+ `size()` was very simple, since the adjacency list is a dictionary. I just had to run a `len()` on the list itself to retrieve its size and return it.
