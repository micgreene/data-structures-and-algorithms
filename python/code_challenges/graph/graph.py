from code_challenges.graph.vertex import Vertex
from code_challenges.graph.edge import Edge

class Graph():
    def __init__(self) -> None:
        self.adj_list = {}

    def __str__(self):
        return (f'a graph defined as:\n{self.adj_list}')

    def add_node(self, value):
        new_vert = Vertex(value)

        self.adj_list[new_vert] = []
        print(self.adj_list)
        return new_vert

    def add_edge(self, start_vert, end_vert=None, weight=None):
        new_edge = Edge(start_vert, end_vert, weight)

        if start_vert in self.adj_list:
            if end_vert in self.adj_list or end_vert is None:
                self.adj_list[start_vert].append(new_edge)
            else:
                raise Exception('ending vertex is not in graph!')
        else:
                raise Exception('starting vertex is not in graph!')

    def get_nodes(self):
        ret_list = []

        for vertex in self.adj_list:
                ret_list.append(vertex)

        return ret_list

    def get_neighbors(self, vert):
        ret_list = []

        for edge in self.adj_list[vert]:
                ret_list.append(edge)
        return ret_list

    def size(self):
        return len(self.adj_list)
