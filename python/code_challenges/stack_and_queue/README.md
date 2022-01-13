# Code Challenge 10 - Stack and a Queue Implementation

## Challenge

**Node**
+ Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.

**Stack**
+ Create a Stack class that has a top property. It creates an empty Stack when instantiated.
  + This object should be aware of a default empty value assigned to top when the stack is created.
+ *The class should contain the following methods:*
  + push
    + Arguments: value
    + adds a new node with that value to the top of the stack with an O(1) Time performance.
  + pop
    + Arguments: none
    + Returns: the value from node from the top of the stack
    + Removes the node from the top of the stack
    + Should raise exception when called on empty stack
  + peek
    + Arguments: none
    + Returns: Value of the node located at the top of the stack
    + Should raise exception when called on empty stack
  + is empty
    + Arguments: none
    + Returns: Boolean indicating whether or not the stack is empty.

**Queue**
+ Create a Queue class that has a front property.
  + It creates an empty Queue when instantiated.
  + This object should be aware of a default empty value assigned to front when the queue is created.
  + The class should contain the following methods:
    + enqueue
      + Arguments: value
        + adds a new node with that value to the back of the queue with an O(1) Time performance.
    + dequeue
      + Arguments: none
        + Returns: the value from node from the front of the queue
        + Removes the node from the front of the queue
        + Should raise exception when called on empty queue
    + peek
      + Arguments: none
        + Returns: Value of the node located at the front of the queue
        + Should raise exception when called on empty stack
    + is empty
      + Arguments: none
        + Returns: Boolean indicating whether or not the queue is empty

### Approach & Efficiency

+ I started by making the Node class quickly.
+ With this, I could test each data structure.
+ I then started with the Queue class
  + I used a whiteboard with objects representing nodes to map out what I specifically wanted to happen for each function. This made it easier to understand what to actually code.
  + I then coded basic functionality for each function.
  + I then did one last pass of each funcion, using the unit test conditions to determine edge cases.
+ I repeated the process with the Stack class, changing my process as the stack only adds and removes nodes from the same location.
