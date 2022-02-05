class Node():
    '''
    Node class for a binary tree.
    '''
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'a Node with a value of {self.value}, a left child with the value of {self.left.value if self.left else None}, and a right child with a value of {self.right.value if self.right else None}'

    def __repr__(self):
        return f'Node(value: {self.value}, left: {self.left.value if self.left else None}, right: {self.right.value if self.right else None})'
