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


def greedy_best_first_search(graph, heuristics, start, goal):
    if start == goal:
        return [start]

    frontier = PriorityQueue()
    explored = set()
    parents = {}

    frontier.put(start, heuristics.get_weight(start, goal))
    parents[start] = None

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parents[current]
            return path[::-1]

        explored.add(current)

        for neighbor in graph.get_neighbors(current):
            if neighbor not in explored and neighbor not in frontier.queue:
                frontier.put(neighbor, heuristics.get_weight(neighbor, goal))
                parents[neighbor] = current

    return None
