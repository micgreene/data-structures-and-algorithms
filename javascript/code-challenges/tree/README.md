# Code challenge 15 - Binary Tree and BST Implementation

## Challenge

- Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
Create a BinaryTree class
Define a method for each of the depth first traversals called preOrder, inOrder, and postOrder which returns an array of the values, ordered appropriately.
Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

Create a BinarySearchTree class
Define a method named add that accepts a value, and adds a new node with that value in the correct location in the binary search tree.
Define a method named contains that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency
I created the two classes in almost exactly the same way:

- First, I based most of the framework after the linklist class we completed previously.
- Using the example from class today, I first outlined all the methods loosely with pseudo code in order to organize my classes.
- After I had a general idea of what each method should do, I used TDD to create each method by ensuring each test case passed. 
