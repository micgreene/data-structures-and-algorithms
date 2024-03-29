# Code Challenge 16 - Find the Maximum Value in a Binary Tree

## Challenge

### Write the following method for the Binary Tree class

+ find maximum value
  + Arguments: none
  + Returns: number
  + Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.

### Whiteboard

![Whiteboard](code_challenge_16.jpg)

### Approach & Efficiency

+ I started by creating a whiteboard visual to clarify what I was trying to do.
+ Essentially, I want to look at every spot in the tree in no particular order and find the largest value.
+ To do this, I thought it would be good to process the nodes from the tree one by one somehow.
+ For this, I figured a queue would work well because of its FIFO functionality.
+ Once the root is inserted into the queue, it is dequeued then its children enqueued in order.
+ The value of the dequeued node is compared against the return node.
+ This process is repeated for each node in the queue until complete.

## Code Challenge 15 - Binary Tree and BST Implementation

### Challenge

### Node

+ Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
+ Binary Tree
  + Create a Binary Tree class
  + Define a method for each of the depth first traversals:
    + pre order
    + in order
    + post order
  + which returns an array of the values, ordered appropriately.
  + Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

+ Binary Search Tree
  + Create a Binary Search Tree class
  + This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
    + Add
      + Arguments: value
      + Return: nothing
      + Adds a new node with that value in the correct location in the binary search tree.
    + Contains
      + Argument: value
      + Returns: boolean indicating whether or not the value is in the tree at least once.

### Approach & Efficiency

+ I started by creating the Node class.
+ I then created the BinaryTree class.
+ The traversals were mostly solved in class so those weren't difficult to implement.
+ I then created the BinarySearch class.
+ For the add function I used a whiteboard to keep track of a while loop iteration that compared the current value to each parent starting from the root.
+ This reminded me somewhat of a quicksort, where we would use the root as a pivot to find which side of the tree the node should be added to depending on the value of the parent node.
+ For the contains function I ran into some traouble as I was trying to use a recursive function to traverse through the tree and it was making it difficult to return a value.
+ I solved this by passing a continer variable to the recursive function the first time it is run to create a pointer to it.
