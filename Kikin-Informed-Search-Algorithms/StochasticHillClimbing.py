"""
From Map to Graph
Universidad Panamericana Campus Mixcoac
Inteligencia Artificial
Enrique Ulises Báez Gómez Tagle
Iván Cruz Ledesma
Mauricio Pérez Aguirre
April 26 2023
v 1.0
R:: Enrique Ulises Báez Gómez Tagle
"""

from random import shuffle
import time


def StochasticHillClimbing(graph, heuristcs, origin, destination):
    start_time = time.time()
    # initialize costs and paths dictionaries with the origin node
    costs = {origin: 0}
    paths = {origin: []}
    # initialize the frontier with the origin node
    frontier = [origin]

    # loop until the frontier is not empty
    while frontier:
        # select the first node in the frontier
        current = frontier.pop(0)
        # check if the current node is the destination node
        if current == destination:
            # print the cost of the solution and return the path
            print(f"Cost: {costs[current]}")
            end_time = time.time()
            print("Tiempo de ejecución: ", end_time - start_time, "segundos")
            return paths[current]

        # loop through the neighbors of the current node
        for destiny in graph.get_neighbors(current):
            # calculate the weight of the edge between the current and the neighbor node
            weight = graph.get_weight(current, destiny)
            # check if the neighbor node has not been visited or if the cost of the path to the neighbor node
            # is lower than the previous cost
            if destiny not in costs or costs[current] + float(weight) < costs[destiny]:
                # update the cost of the path to the neighbor node
                costs[destiny] = costs[current] + float(weight)
                # update the path to the neighbor node
                paths[destiny] = paths[current] + [destiny]
                # add the neighbor node to the frontier
                frontier.append(destiny)

        # shuffle the frontier randomly
        shuffle(frontier)
        # sort the frontier based on the cost of the path plus the heuristic estimate of the next node
        frontier.sort(key=lambda x: costs[x] + float(
            heuristcs.nodes[current][list(heuristcs.get_neighbors(current))[0]]))
        # limit the frontier to the 10 lowest cost nodes
        frontier = frontier[:10]

    end_time = time.time()
    print("Tiempo de ejecución: ", end_time - start_time, "segundos")
    return None
