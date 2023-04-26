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

from random import shuffle


def StochasticHillClimbing(graph, heuristcs, origin, destination):
    costs = {origin: 0}
    paths = {origin: []}
    frontier = [origin]

    while frontier:
        current = frontier.pop(0)
        if current == destination:
            print(f"Cost: {costs[current]}")
            return paths[current]

        for destiny in graph.get_neighbors(current):
            weight = graph.get_weight(current, destiny)
            if destiny not in costs or costs[current] + float(weight) < costs[destiny]:
                costs[destiny] = costs[current] + float(weight)
                paths[destiny] = paths[current] + [destiny]
                frontier.append(destiny)

        shuffle(frontier)
        frontier.sort(key=lambda x: costs[x] + float(
            heuristcs.nodes[current][list(heuristcs.get_neighbors(current))[0]]))
        frontier = frontier[:10]

    return None
