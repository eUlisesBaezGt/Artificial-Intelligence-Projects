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


def BranchAndBound(graph, origin, destination):
    visited = set()
    frontier = PriorityQueue()
    # Tuple contains the current path cost, current node, and the path so far
    frontier.put((0, origin, [origin]))
    while not frontier.empty():
        cost, node, path = frontier.get()
        if node == destination:
            print(f"Cost: {cost}")
            return path
        visited.add(node)
        for neighbor, weight in graph.nodes[node].items():
            if neighbor not in visited:
                new_path = path + [neighbor]
                bound = cost + int(weight)
                frontier.put((bound, neighbor, new_path))
    return None
