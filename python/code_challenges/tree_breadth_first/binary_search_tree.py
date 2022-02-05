from binary_tree import BinaryTree
from tree_node import Node

class BinarySearch(BinaryTree):

    def add(self, val):
        '''
        This function adds a new value to a Binary Search Tree. Since it is a BST, this means:
        1) items less than the value of the root will be added as children to the left of the root
        2) items greater than or equal to the value of the root will be added as children to the right of the root
        3)  item is stored as the left child of a parent with a greater value or as the right child of a parent with a lesser value.

        Input: val as an int
        Output: None
        '''
        root=5


        node = Node(val)

        if self.root == None:
            self.root = node
            return

        currentNode = self.root
        trackingNode = None

        while currentNode != None:
            trackingNode = currentNode
            if val < currentNode.value:
                currentNode = currentNode.left

            else:
                currentNode = currentNode.right

        if val < trackingNode.value:
            trackingNode.left = node
        else:
            trackingNode.right = node


    def contains(self, val):
        '''
        This function returns a boolean confirming whether the tree already contains the passed input value.

        Input: val as an int
        Output: boolean
        '''
        if self.root == None:
            raise Exception('Empty Tree!')

        d = {"contained": False}

        def walk(node,contained):
            if node.value == val:
                contained["contained" ] = True

            if node.left: walk(node.left,contained)
            if node.right: walk(node.right,contained)

        walk(self.root, d)
        return d["contained"]
