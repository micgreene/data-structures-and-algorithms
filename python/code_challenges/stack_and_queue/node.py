class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return f'a Node with a value of {self.value}'

    def __repr__(self):
        return f'Node(value: {self.value}, next: {self.next})'
