from graph import Graph
from vertex import Vertex

def business_trip(graph_map, itinerary):
    ret_sum = 0
    step = 2
    connects = False

    if graph_map.size() < 2:
        ret_list = [connects, '$0']
        return ret_list
    elif len(itinerary) < 2:
        ret_list = [connects, '$0']
        return ret_list

    depart = itinerary[0]
    arrival = itinerary[1]

    while arrival is not None:
        depart = Vertex(depart)
        connects = False
        connections = graph_map.get_neighbors(depart.value)

        if len(connections) > 0:
            for i in range(len(connections)):
                if connections[i].end_vert.value == arrival:
                    connects = True
                    ret_sum += connections[i].weight
                    depart = arrival
                elif i == len(connections) - 1 and connects == False:
                    ret_list = [connects, '$0']
                    return ret_list
            try:
                arrival = itinerary[step]
                step = step + 1
            except:
                arrival = None

        else:
            ret_list = [connects, '$0']
            return ret_list

    ret_list = [connects, f'${ret_sum}']
    return ret_list
