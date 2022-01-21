class Node:
    '''
    Node class for storing values in our stack.
    Attributes:
        self.value: any value
        self.next: pointer to next node in dataset
    '''
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return f'a Node with a value of {self.value}'

    def __repr__(self):
        return f'Node(value: {self.value}, next: {self.next})'
