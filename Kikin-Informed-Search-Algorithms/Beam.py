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
import time


def BeamSearch(graph, heuristics, start, goal):
    # get the beam width from the user
    beam_width = int(input("Beam Width: "))
    start_time = time.time()

    # if the start node is the same as the goal node, return the start node as the solution
    if start == goal:
        return [start]

    # initialize the priority queue with the start node and its priority
    frontier = PriorityQueue()
    explored = set()
    parents = {}
    frontier.put((start, 0))
    parents[start] = None

    while not frontier.empty():
        # select the top k nodes from the priority queue
        candidates = []
        for _ in range(beam_width):
            if not frontier.empty():
                candidates.append(frontier.get())

        for candidate, _ in candidates:
            # if the goal node has been reached, reconstruct the path and return it
            if candidate == goal:
                path = []
                while candidate is not None:
                    path.append(candidate)
                    candidate = parents[candidate]
                return path[::-1]

            # add the current node to the set of explored nodes
            explored.add(candidate)

            # expand the current node by visiting its neighboring nodes
            for neighbor in graph.get_neighbors(candidate):
                # if the neighbor has not been explored, calculate its priority and add it to the priority queue
                if neighbor not in explored:
                    new_cost = heuristics.get_weight(neighbor, goal)
                    priority = new_cost
                    frontier.put((neighbor, priority))
                    # keep track of the parent node to reconstruct the path later
                    parents[neighbor] = candidate

    end_time = time.time()
    print("Exec time: ", end_time - start_time, "segundos")
    # if no solution is found, return None
    return None
