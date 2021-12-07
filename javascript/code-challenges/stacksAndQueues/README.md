# Stacks and Queues
- Code challenge 10 - create 2 classes, Stack and Queue, which use a 3rd class, Node, as items in their storages. 

- We then create several methods to add and remove items from the stack(FILO) and queue(FIFO).

## Challenge
- Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
- **Create a Stack class** that has a top property. It creates an empty Stack when instantiated.
This object should be aware of a default empty value assigned to *top* when the stack is created.
- Define a method called *push* which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.
- Define a method called *pop* that does not take any argument, removes the node from the top of the stack, and returns the node’s value.
Should raise exception when called on empty stack
- Define a method called *peek* that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.
- Should raise exception when called on empty stack
- Define a method called *isEmpty* that takes no argument, and returns a boolean indicating whether or not the stack is empty.

- **Create a Queue class** that has a front property. It creates an empty Queue when instantiated.
This object should be aware of a default empty value assigned to *front* when the queue is created.
- Define a method called *enqueue* which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.
- Define a method called *dequeue* that does not take any argument, removes the node from the front of the queue, and returns the node’s value.
- Should raise exception when called on empty queue
- Define a method called *peek* that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.
- Should raise exception when called on empty queue
- Define a method called *isEmpty* that takes no argument, and returns a boolean indicating whether or not the queue is empty.

## Approach & Efficiency
I created the two classes in almost exactly the same way:

- First, I based most of the framework after the linklist class we completed previously.
- Using the example from class today, I first outlined all the methods loosely with pseudo code in order to organize my classes.
- After I had a general idea of what each method should do, I used TDD to create each method by ensuring each test case passed. 
