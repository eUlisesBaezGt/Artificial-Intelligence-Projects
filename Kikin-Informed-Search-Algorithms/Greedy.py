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


def greedy_best_first_search(graph, heuristics, start, goal):
    start_time = time.time()
    # If the start node is the same as the goal node, return a list containing just the start node
    if start == goal:
        
        end_time = time.time()
        print("Tiempo de ejecución: ", end_time - start_time, "segundos")   
        return [start]

    # Create a priority queue to store the nodes we need to explore
    frontier = PriorityQueue()
    # Create a set to keep track of explored nodes
    explored = set()
    # Create a dictionary to keep track of the parent of each node
    parents = {}

    # Add the start node to the priority queue, along with its estimated cost to the goal node (as determined by the heuristic function)
    frontier.put(start, heuristics.get_weight(start, goal))
    # Set the parent of the start node to None
    parents[start] = None

    # Continue exploring nodes in the priority queue until it is empty
    while not frontier.empty():
        # Get the node with the lowest estimated cost to the goal from the priority queue
        current = frontier.get()

        # If we have reached the goal node, construct and return the path from the start to the goal
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parents[current]
            # Return the path in reverse order (from start to goal)
            
            end_time = time.time()
            print("Tiempo de ejecución: ", end_time - start_time, "segundos")
            return path[::-1]

        # Add the current node to the set of explored nodes
        explored.add(current)

        # For each neighbor of the current node
        for neighbor in graph.get_neighbors(current):
            # If the neighbor has not been explored and is not already in the priority queue
            if neighbor not in explored and neighbor not in frontier.queue:
                # Add the neighbor to the priority queue, along with its estimated cost to the goal (as determined by the heuristic function)
                frontier.put(neighbor, heuristics.get_weight(neighbor, goal))
                # Set the parent of the neighbor to the current node
                parents[neighbor] = current

    # If we have explored all possible paths and have not found a path to the goal node, return None
    
    end_time = time.time()
    print("Tiempo de ejecución: ", end_time - start_time, "segundos")
    return None

