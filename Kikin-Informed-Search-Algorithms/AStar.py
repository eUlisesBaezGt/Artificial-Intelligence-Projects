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


def AStarSearch(graph, heuristics, origin, destination):
    frontier = PriorityQueue()
    frontier.put(origin, heuristics.get_weight(origin, destination))
    came_from = {}
    cost_so_far = {origin: 0}

    while not frontier.empty():
        current = frontier.get()

        if current == destination:
            break

        for next_node in graph.get_neighbors(current):
            new_cost = cost_so_far[current] + \
                int(graph.get_weight(current, next_node))
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + \
                    float(heuristics.get_weight(next_node, destination))
                frontier.put(next_node, priority)
                came_from[next_node] = current  # Reconstruct the path
    path = [destination]
    while path[-1] != origin:
        path.append(came_from[path[-1]])
    path.reverse()
    print(f"Cost: {cost_so_far[destination]}")
    return path
