from code_challenges.trees.tree_node import Node
from code_challenges.trees.queue import Queue

class BinaryTree():
    def __init__(self, root=None):
        self.root = Node(root)

    def __str__(self):
        return f'A Binary Tree, its root has a value of {self.root.value}'

    def __repr__(self):
        return f'BinaryTree(root: {self.root.value})'

    def pre_order(self):
        '''
        Returns a pre-ordered list of the tree's node values.

        Input: None
        Output: list
        '''
        if self.root == None:
            raise Exception('Empty Tree!')

        nodes = []
        def walk(node):
            nodes.append(node.value)
            if node.left: walk(node.left)
            if node.right: walk(node.right)

        walk(self.root)

        return nodes

    def in_order(self):
        '''
        Returns a in-ordered list of the tree's node values.

        Input: None
        Output: list
        '''
        if self.root == None:
            raise Exception('Empty Tree!')

        nodes = []
        def walk(node):
            if node.left: walk(node.left)
            nodes.append(node.value)
            if node.right: walk(node.right)

        walk(self.root)

        return nodes

    def post_order(self):
        '''
        Returns a post-ordered list of the tree's node values.

        Input: None
        Output: list
        '''
        if self.root == None:
            raise Exception('Empty Tree!')

        nodes = []
        def walk(node):
            if node.left: walk(node.left)
            if node.right: walk(node.right)
            nodes.append(node.value)

        walk(self.root)

        return nodes
