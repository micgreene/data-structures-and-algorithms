from code_challenges.graph_business_trip.graph import Graph

def business_trip(graph_map, itinerary):
    '''
    Takes in a graph representing a map of connecting airports, and a list of cities which acts as an "itinerary". If all airports in the itinerary are able to be traversed to using the graph, return a list containing a boolean and a sum of the weights of the edges between the node vertices (the airfare).
    Input: graph, list
    Output: list = [bool, string]
    '''
    ret_sum = 0
    # step is used to ensure we don't go out of index when checking our list of connections
    step = 2
    # tracks if we are able to connect to the next expected location in our itinerary
    connects = False

    # Edge Cases - if itinerary or map don't have enough destinations, return False
    if graph_map.size() < 2:
        ret_list = [connects, '$0']
        return ret_list
    elif len(itinerary) < 2:
        ret_list = [connects, '$0']
        return ret_list

    # create two pointers tracking which departure/arrival pair we are looking at
    depart = itinerary[0]
    arrival = itinerary[1]

    while arrival is not None:
        connects = False
        connections = graph_map.get_neighbors(depart)

        # if this location has no locations then we cannot continue the trip and return false
        if len(connections) > 0:
            for i in range(len(connections)):
                # if we can find a connection, accumulate the airfare sum, affirm we are able to connect, and change our depature location to our current arrival location
                if connections[i].end_vert.value == arrival:
                    connects = True
                    ret_sum += connections[i].weight
                    depart = arrival
                # if we have reached the end of the connections list and cannot connect to any new locations then we cannot continue the trip and return False
                elif i == len(connections) - 1 and connects == False:
                    ret_list = [connects, '$0']
                    return ret_list
            # once all connections have been looked at, change our arrival location to the next step of our itinerary list, and increment step by 1.
            try:
                arrival = itinerary[step]
                step = step + 1
            # if we can't reassign arrival, it is because we are at the end of our itinerary. we reassign arrival to None to exit the while loop
            except:
                arrival = None

        else:
            ret_list = [connects, '$0']
            return ret_list
    # if we have completed the while loop, then we have arrived at our destination.
    # return True and the total airfare sum
    ret_list = [connects, f'${ret_sum}']
    return ret_list
