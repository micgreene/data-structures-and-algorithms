class Node():
    '''
    Node class for a queue.
    '''
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f'a Node with a value of {self.value}, a pointer to a next with a value of {self.next.value if self.next else None}'

    def __repr__(self):
        return f'Node(value: {self.value}, next: {self.next.value if self.next else None})'
