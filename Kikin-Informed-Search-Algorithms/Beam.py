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


def BeamSearch(graph, heuristics, start, goal):
    beam_width = int(input("Beam Width: "))

    if start == goal:
        return [start]

    frontier = PriorityQueue()
    explored = set()
    parents = {}

    frontier.put((start, 0))
    parents[start] = None

    while not frontier.empty():
        candidates = []
        for _ in range(beam_width):
            if not frontier.empty():
                candidates.append(frontier.get())

        for candidate, _ in candidates:
            if candidate == goal:
                path = []
                while candidate is not None:
                    path.append(candidate)
                    candidate = parents[candidate]
                return path[::-1]

            explored.add(candidate)

            for neighbor in graph.get_neighbors(candidate):
                if neighbor not in explored:
                    new_cost = heuristics.get_weight(neighbor, goal)
                    priority = new_cost
                    frontier.put((neighbor, priority))
                    parents[neighbor] = candidate

    return None
