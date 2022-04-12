from code_challenges.graph.vertex import Vertex
from code_challenges.graph.edge import Edge
from code_challenges.graph.queue import Queue
from code_challenges.graph.stack import Stack

class Graph():
    '''
    A data structure implentation of a graph, or a collection of nodes each with a collection of edges which direct a connection between two vertices and track a weight value.
    '''
    def __init__(self) -> None:
        self.adj_list = {}

    def __str__(self):
        return (f'a graph defined as:\n{self.adj_list}')

    def __repr__(self):
        return (f'Graph({self.adj_list})')

    def add_node(self, value):
        '''
        Adds a new vertex to the graph.
        Input: value as any given value
        Output: the added node instance
        '''
        new_vert = Vertex(value)

        self.adj_list[new_vert] = []

        return new_vert

    def add_edge(self, start_vert, end_vert=None, weight=None):
        '''
        Adds a directed edge between two vertices to the graph. Also accepts a weight value for the edge.
        Input: start_vert as the starting node
               end_vert as the ending node
               weight as the weight value, default of None
        Output: None
        '''
        new_edge = Edge(start_vert, end_vert, weight)

        if start_vert in self.adj_list:
            if end_vert in self.adj_list or end_vert is None:
                self.adj_list[start_vert].append(new_edge)
            else:
                # exceptions are raised if the given node cannot be found in the graph
                raise Exception('ending vertex is not in graph!')
        else:
                raise Exception('starting vertex is not in graph!')

    def get_nodes(self):
        '''
        Returns a list of nodes in the graph.
        Input: None
        Output: a list of node values
        '''
        ret_list = []

        for vertex in self.adj_list:
                ret_list.append(vertex)

        return ret_list

    def get_neighbors(self, vert):
        '''
        Returns a list of edges belonging to a given vertex.
        Input: vert as an instance of a vertex that exists in the adjacency list.
        Output: a list of edges
        '''
        ret_list = []

        for edge in self.adj_list[vert]:
                ret_list.append(edge)
        return ret_list

    def breadth_first(self, vert):
        '''
        Given a node, returns a collection of breadth-first ordered nodes that can be reached from the given node.
        Input: Node
        Output: List of Nodes
        '''
        vert_queue = Queue()
        vert_queue.enqueue(vert)
        ret_list = []
        temp_adj_list = self.adj_list


        #continues enqueuing nodes in the order you encounter them, while loop continues until queue is empty
        while vert_queue.is_empty() is not True:
            temp = vert_queue.dequeue()

            # if the node is not in the adjacency list (or is None), we'll just return it in a list by itself
            if temp not in ret_list:
                ret_list.append(temp)

                if temp in temp_adj_list:
                    # we create a clone adjency list (temp_adj_list) and use it to preserve original dat structure
                    temp_children = temp_adj_list[temp]
                    for vert in temp_children:
                        # takes the end_vert property from the edge to determine the node adjacency
                        vert_queue.enqueue(vert.end_vert)
                else:
                    return ret_list
        return ret_list

    def depth_first(self, node):
        '''
        Given a node, returns a collection of depth-first pre-ordered nodes that can be reached from the given node.
        Input: Node
        Output: List of Nodes
        '''
        if node == None:
            return [None]
        elif len(self.get_neighbors(node)) == 0:
            return [node]

        ret_list = []
        node_stack = Stack()

        node_stack.push(node)

        while node_stack.is_empty() is not True:
            # pop last node off of stack, this ensures we stay in pre-ordered collection. We never look at the first encountered node in the list of children, always the last.
            temp = node_stack.pop()
            if temp in ret_list:
                pass
            else:
                ret_list.append(temp)
                temp_children = self.get_neighbors(temp)
                if len(temp_children) > 0:
                    for edge in temp_children:
                        node_stack.push(edge.end_vert)

        return ret_list

    def size(self):
        '''
        Returns how many nodes are in the graph.
        Input: None
        Output: integer value of items in graph
        '''
        return len(self.adj_list)
