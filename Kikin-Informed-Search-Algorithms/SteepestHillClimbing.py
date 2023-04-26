"""
From Map to Graph
Universidad Panamericana Campus Mixcoac
Inteligencia Artificial
Enrique Ulises Báez Gómez Tagle
Iván Cruz Ledesma
Mauricio Pérez Aguirre
April 26 2023
v 1.0
Main file where you can select the algorithm you want to use.
To use this file, please install our package and run file from console.
To run file, go to folder where this file is located and run:
python main.py
"""
import time

def SteepestHillClimbing(graph, heuristcs, origin, destination):
    start_time = time.time()
    # Initialize costs, paths, and frontier
    costs = {origin: 0}
    paths = {origin: []}
    frontier = [origin]

    # Loop until the frontier is empty
    while frontier:
        # Sort the frontier based on the sum of the cost and heuristic value for each node
        frontier.sort(key=lambda node: costs[node] + float(
            heuristcs.nodes[node][list(heuristcs.nodes[node].keys())[0]]))
        current = frontier.pop(0)

        # Check if the current node is the destination node
        if current == destination:
            # Print the cost and return the optimal path
            print(f"Cost: {costs[current]}")
            end_time = time.time()
            print("Tiempo de ejecución: ", end_time - start_time, "segundos")
            return paths[current] + [current]

        # Expand the current node
        for next_node in graph.get_neighbors(current):
            weight = graph.get_weight(current, next_node)
            cost = costs[current] + int(weight)
            if next_node not in costs or cost < costs[next_node]:
                # Update the cost and path for the next node if a better path is found
                costs[next_node] = cost
                paths[next_node] = paths[current] + [current]
                if next_node not in frontier:
                    # Add the next node to the frontier if it's not already there
                    frontier.append(next_node)

    # If no path is found, return None

    end_time = time.time()
    print("Tiempo de ejecución: ", end_time - start_time, "segundos")
    return None
