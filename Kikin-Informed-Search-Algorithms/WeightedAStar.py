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

from queue import PriorityQueue


def WeightedAStarSearch(graph, heuristics, origin, destination):
    # Asks the user for the weight value to be used in the search.
    weight = float(input("Enter w value: "))

    # Initializes the frontier queue and adds the starting node with its heuristic cost.
    frontier = PriorityQueue()
    frontier.put(origin, heuristics.get_weight(origin, destination))

    # Initializes the dictionaries that will store the cost so far and the paths to each node.
    came_from = {}
    cost_so_far = {origin: 0}

    # Iterates while there are still nodes in the frontier queue.
    while not frontier.empty():
        # Gets the node with the lowest priority from the frontier queue.
        current = frontier.get()

        # If the goal node has been reached, breaks out of the loop.
        if current == destination:
            break

        # Iterates through the neighbors of the current node.
        for next_node in graph.get_neighbors(current):
            # Calculates the new cost for reaching the neighbor.
            new_cost = cost_so_far[current] + weight * \
                (float(graph.get_weight(current, next_node)))

            # If the neighbor has not been visited yet or the new cost is lower than the current cost, updates the cost and priority for the neighbor.
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + weight * \
                    (float(heuristics.get_weight(next_node, destination)))
                frontier.put(next_node, priority)
                came_from[next_node] = current

    # Reconstructs the path from the start to the goal node.
    path = [destination]
    while path[-1] != origin:
        path.append(came_from[path[-1]])
    path.reverse()

    # Prints the cost of the path and returns the path.
    print(f"Cost: {cost_so_far[destination]}")
    return path
