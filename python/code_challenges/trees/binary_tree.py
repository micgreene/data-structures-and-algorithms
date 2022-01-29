from tree_node import Node
from queue import Queue

class BinaryTree():
    def __init__(self, root=None):
        self.root = Node(root)

    def __str__(self):
        return f'A Binary Tree, its root has a value of {self.root.value}'

    def __repr__(self):
        return f'BinaryTree(root: {self.root.value})'

    def pre_order(self):
        if self.root == None:
            raise Exception('Empty Tree!')

        nodes = []

        _walk = def (node):
            nodes.push(node.value)
            if node.left: _walk(node.left)
            if node.right: _walk(node.right)
        _walk(this.root)

        return nodes

    def in_order(self, node):
        return

    def post_order(self, node):
        return

tree = BinaryTree(5)
node6 = Node(6)
node7 = Node(7)
tree.root.left = node6
tree.root.right = node7
tree.pre_order()




