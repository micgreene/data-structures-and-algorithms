class Vertex():
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return f'a node vertex with a value of {self.value}'

    def __repr__(self):
        return f'Vertex({self.value})'
