# Graph Class

## Implement a Graph

### Challenge

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
