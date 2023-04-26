"""
From Map to Graph
Universidad Panamericana Campus Mixcoac
Inteligencia Artificial
Enrique Ulises Báez Gómez Tagle
Iván Cruz Ledesma
Mauricio Pérez Aguirre
April 26 2023
v 1.0
R:: Mauricio Pérez Aguirre
"""

from queue import PriorityQueue
import time


def BranchAndBound(graph, origin, destination):
    start_time = time.time()
    # Create an empty set to keep track of visited nodes
    visited = set()
    # Create a priority queue to store the nodes we need to explore
    frontier = PriorityQueue()
    # Add the origin node to the priority queue, along with its path and cost (which is initially 0)
    frontier.put((0, origin, [origin]))

    # Continue exploring nodes in the priority queue until it is empty
    while not frontier.empty():
        # Get the node with the lowest bound (i.e., estimated cost) from the priority queue
        cost, node, path = frontier.get()
        # If we have reached the destination node, print the cost and return the path
        if node == destination:
            print(f"Cost: {cost}")
            end_time = time.time()
            print("Tiempo de ejecución: ", end_time - start_time, "segundos")
            return path
        # Add the current node to the set of visited nodes
        visited.add(node)
        # For each neighbor of the current node that has not been visited yet
        for neighbor, weight in graph.nodes[node].items():
            if neighbor not in visited:
                # Create a new path that includes the neighbor node
                new_path = path + [neighbor]
                # Calculate the bound (i.e., estimated cost) of the new path
                bound = cost + int(weight)
                # Add the new path and bound to the priority queue
                frontier.put((bound, neighbor, new_path))
    # If we have explored all possible paths and have not found a path to the destination node, return None
    end_time = time.time()
    print("Tiempo de ejecución: ", end_time - start_time, "segundos")
    return None
