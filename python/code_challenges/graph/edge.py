class Edge():
    def __init__(self, start_vert, end_vert=None, weight=0):
        self.start_vert = start_vert
        self.end_vert =end_vert
        self.weight = weight

    def __str__(self):
        return f'an edge between {self.start_vert} and {self.end_vert}, with a weight of {self.weight}'

    def __repr__(self):
        return f'Edge({self.start_vert, self.end_vert, self.weight})'
