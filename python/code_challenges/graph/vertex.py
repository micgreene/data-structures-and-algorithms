class Vertex():
    '''
    This class acts as a single vertex in a graph, containing just a value.
    '''
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return f'a node vertex with a value of {self.value}'

    def __repr__(self):
        return f'Vertex({self.value})'
